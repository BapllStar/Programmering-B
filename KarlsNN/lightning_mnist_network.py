from mnist_network import ThatMnistNet, collate_fn, get_and_process_data
import lightning as L
import torch
# From the creators who brought you lightning, prepare for torchmetrics...
from torchmetrics.functional import accuracy
from torch.utils.data import DataLoader

class LightningMnistNet(L.LightningModule):
    def __init__(self, in_features=28*28, out_features=10, lr=0.001, scuffed_version=False):
        """
        Like the other one but waaaay cooler
        So basically, Lightning just implements a lot of functionality under the hood
        I reccommend using it when you've grasped what Torch does... overall

        Things you DON'T need to do with lightning models:
        1. Make sure data/model is both on cuda/cpu - it does this automatically
        2. Write a training loop - it does this automatically

        """

        super().__init__()
        self.model = ThatMnistNet(in_dim=28*28, out_dim=10)
        self.train_set, self.test_set = get_and_process_data()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        We really technically don't need a forward function
        Since we can just call self.model(input) in training_step and evaluate
        But we're lazy....
        """
        return self.model(x)
        
    def training_step(self, batch):
        """
        A training step in lightning only needs to calculate and return the loss
        Everything else is handled, under the hood
        """

        x, y = batch
        logits = self(x)
        loss = self.model.criterion(logits, y)

        # Honestly, I don't remember where the logs end up...
        self.log("train_loss", loss)
        return loss

    def evaluate(self, batch, stage=None):
        """
        Just a single evaluation step... so this is meant for finding accuracy, not getting updates
        """

        x, y = batch
        logits = self(x)
        loss = self.criterion(logits, y.to(torch.long))
        preds = torch.argmax(logits, dim=1)
        acc = accuracy(preds, y, task="multiclass", num_classes=10)

        if stage:
            self.log(f"{stage}_loss", loss, prog_bar=True)
            self.log(f"{stage}_acc", acc, prog_bar=True)
    
    """
    I don't quite remember if both below are actually necessary
    But I made this a while ago...
    """

    def validation_step(self, batch):
        self.evaluate(batch, "val")

    def test_step(self, batch, batch_idx):
        self.evaluate(batch, "test") 

    def configure_optimizers(self):
        """
        Necessary since Lightning does not inherit the optimizers of whatever model it uses, it needs its own
        """

        optimizer = torch.optim.Adam(
            self.model.parameters(),
        )
        return {"optimizer": optimizer}


    """
    All these below are necessary unless you really wanna specify your own data loaders for the trainer module in PyTorch?
    """
    def train_dataloader(self):
        train_loader = torch.utils.data.DataLoader(self.train_set, shuffle=True, collate_fn=collate_fn, batch_size=16)
        return train_loader
    
    def test_dataloader(self):
        test_loader = torch.utils.data.DataLoader(self.test_set, shuffle=True, collate_fn=collate_fn, batch_size=16)
        return test_loader
    
if __name__ == "__main__":
    model = LightningMnistNet()
    trainer = L.Trainer()
    # WARNING: WON'T WORK IF YOU HAVE DEFINED HTE TRAIN FUNCTION FOR THE MNIST_NETWORK, otherwise lightining, will see
    # that its model alreayd has a train function and be all like 'oooh, iz free real estate'
    # so we need to comment it out when we use lightning, otherwise we won't use lightning's zpicy training functions
    # again, we could fix this in a better way...
    # but... we're lazy
    trainer.fit(model)
    trainer.test()