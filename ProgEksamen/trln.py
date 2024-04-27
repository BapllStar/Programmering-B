def træn(self, 
         inputs : np.ndarray,           # En liste med input til netværket
         ønskede_outputs : np.ndarray,  # En liste med ønskede output til netværket
         skridt_længde : float,         # Skridtlængden for gradientnedstigning
         epoker : int,                  # Antal skridt for gradientnedstigning
         batchstørrelse : int,          # Hvor nøjagtig gradientnedstigning skal være
         tab_print_interval : int,      # Hvor ofte skal tabet printes i konsollen
         ) -> None:

        
        sidste_tab = 0 

        # Mini-batch gradientnedstigning.
        i = 0
        for epoke in range(epoker): 
            # For hver epoke

            for batch in range(batchstørrelse): 
                # For hver batch

                output = self.frem(inputs[i % len(inputs)])
                # Inputtet sendes igennem netværket, og outputtet returneres.

                pa_output = pa_tab(output, ønskede_outputs[i % len(ønskede_outputs)])
                # Den partielle afledte af tabet for outputtet udregnes. 
                # Dette bruges til at finde ud af, hvor meget de forskellige vægte og biaser skal ændres.

                self.__tilbage(pa_output)
                # Backpropagation. Her udrenger vi de ændringer, der skal laves til dette eksempel.
                # Endringerne bliver gemt i de individuelle lag

                

                i += 1

            # Print tabet i konsollen, hvis det er tid til det.
            if (epoke+1) % tab_print_interval == 0:
                tab = self.__tab(output, ønskede_outputs[i % len(ønskede_outputs)])
                print(f"Epoke {epoke+1}/{epoker} | {np.round(100*(epoke+1)/epoker,2)}% | Tab: {tab} | Ændring: {tab - sidste_tab}")

                sidste_tab = tab
            
            self.__update(skridt_længde)
            # Efter at have kørt en batch igennem, opdateres vægtene og biaserne i hele netværket.
            
            
        
        print("\nTræning færdig")
        print(f"Afsluttet med tab: {self.__tab(output, ønskede_outputs[i % len(ønskede_outputs)])}")