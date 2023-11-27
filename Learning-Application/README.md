<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Læringsapp</title>
  <link rel="stylesheet" href="https://stackedit.io/style.css" />
</head>

<body class="stackedit">
  <div class="stackedit__html"><h1 id="learning-application">Learning Application</h1>
<p>I dette dokument, kan du læse om <a href="https://github.com/BapllStar/Programmering-B/tree/main/Learning-Application">mit projekt</a>.</p>
<h2 id="programmets-formål">Programmets formål</h2>
<p>Jeg vil udvikle en app, der træner dens brugere i hovedregning. Dette gøres ved at holde en score for, hvor godt brugeren klarer sig, og give opgaver, der svarer til nivauet.<br>
Selv projektet kan du finde <a href="https://github.com/BapllStar/Programmering-B/tree/main/Learning-Application">her</a>.</p>
<h2 id="målgruppen">Målgruppen</h2>
<p>Målgruppen er hovedsagligt elever i starten af udskolingen, men da programmet tilpasser sig en sværhedsgrad til den individuelle bruger, bør man teknisk set godt kunne bruge de, så længe man kan addere og subtrahere.</p>
<h2 id="design-pattern----builder">Design Pattern – Builder</h2>
<p>Builder Pattern er et meget simpelt designmønster, der går ud på at bygge klasser ved hjælp af specifikke metoder der returnerer sig selv, så man kan kæde metoderne sammen, hvilket giver mere overskuelighed.</p>
<h3 id="eksempel-på-builder-pattern">Eksempel på Builder Pattern</h3>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">class</span> <span class="token class-name">Hotdog</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
	<span class="token keyword">def</span> <span class="token function">__innit__</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
		self<span class="token punctuation">.</span>bread <span class="token operator">=</span> <span class="token string">""</span>
		self<span class="token punctuation">.</span>sausage <span class="token operator">=</span> <span class="token string">""</span>

	<span class="token keyword">def</span> <span class="token function">add_wheat_bread</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
		self<span class="token punctuation">.</span>bread <span class="token operator">=</span> <span class="token string">"Wheat"</span>
		<span class="token keyword">return</span> self
		<span class="token comment"># Metoden returnerer sig selv, så man kan kæde</span>
		<span class="token comment"># flere af disse buildermetoder sammen på samme</span>
		<span class="token comment"># linje.</span>

	<span class="token keyword">def</span> <span class="token function">add_frankfurter</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
		self<span class="token punctuation">.</span>sausage <span class="token operator">=</span> <span class="token string">"Frankfurter"</span>
		<span class="token keyword">return</span> self
</code></pre>
<pre class=" language-python"><code class="prism  language-python">my_hotdog <span class="token operator">=</span> Hotdog<span class="token punctuation">(</span><span class="token punctuation">)</span>
my_hotdog<span class="token punctuation">.</span>add_what_bread<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">.</span>add_frankfurter<span class="token punctuation">(</span><span class="token punctuation">)</span>
<span class="token comment"># Her kædes de to buildermetoder sammen.</span>
</code></pre>
<hr>
<p>Hvis disse metoder ikke returnerede <code>self</code>, ville man være nødt til at splitte samme funktionalitet over flere linjer:</p>
<pre class=" language-python"><code class="prism  language-python">my_hotdog <span class="token operator">=</span> Hotdog<span class="token punctuation">(</span><span class="token punctuation">)</span>
my_hotdog<span class="token punctuation">.</span>add_wheat_bread<span class="token punctuation">(</span><span class="token punctuation">)</span>
my_hotdog<span class="token punctuation">.</span>add_frankfurter<span class="token punctuation">(</span><span class="token punctuation">)</span>
</code></pre>
<p>Lige specifikt i dette tilfælde er det ikke så slemt, men med flere variabler, kan de gå hen og dække over ret mange linjer.</p>
<h3 id="uden-builder-pattern">Uden Builder Pattern</h3>
<pre class=" language-python"><code class="prism  language-python">skole <span class="token operator">=</span> Skole<span class="token punctuation">(</span><span class="token punctuation">)</span>

klasse_a <span class="token operator">=</span> Klasse<span class="token punctuation">(</span><span class="token punctuation">)</span>

klasse_a<span class="token punctuation">.</span>add<span class="token punctuation">(</span><span class="token string">"Laura"</span><span class="token punctuation">)</span>
klasse_a<span class="token punctuation">.</span>add<span class="token punctuation">(</span><span class="token string">"Lucas"</span><span class="token punctuation">)</span>
klasse_a<span class="token punctuation">.</span>add<span class="token punctuation">(</span><span class="token string">"Matthias"</span><span class="token punctuation">)</span>
klasse_a<span class="token punctuation">.</span>add<span class="token punctuation">(</span><span class="token string">"Marcus"</span><span class="token punctuation">)</span>

klasse_b <span class="token operator">=</span> Klasse<span class="token punctuation">(</span><span class="token punctuation">)</span>

klasse_b<span class="token punctuation">.</span>add<span class="token punctuation">(</span><span class="token string">"William"</span><span class="token punctuation">)</span>
klasse_b<span class="token punctuation">.</span>add<span class="token punctuation">(</span><span class="token string">"David"</span><span class="token punctuation">)</span>
klasse_b<span class="token punctuation">.</span>add<span class="token punctuation">(</span><span class="token string">"Asta"</span><span class="token punctuation">)</span>
klasse_b<span class="token punctuation">.</span>add<span class="token punctuation">(</span><span class="token string">"Sofie"</span><span class="token punctuation">)</span>
klasse_b<span class="token punctuation">.</span>add<span class="token punctuation">(</span><span class="token string">"Albert"</span><span class="token punctuation">)</span>
klasse_b<span class="token punctuation">.</span>add<span class="token punctuation">(</span><span class="token string">"Karla"</span><span class="token punctuation">)</span>

skole<span class="token punctuation">.</span>klasser<span class="token punctuation">.</span>append<span class="token punctuation">(</span>klasse_a<span class="token punctuation">)</span>
skole<span class="token punctuation">.</span>klasser<span class="token punctuation">.</span>append<span class="token punctuation">(</span>klasse_b<span class="token punctuation">)</span>
</code></pre>
<h3 id="med-builder-pattern">Med Builder Pattern</h3>
<pre class=" language-python"><code class="prism  language-python">skole <span class="token operator">=</span> Skole<span class="token punctuation">(</span><span class="token punctuation">)</span>
skole<span class="token punctuation">.</span>klasser<span class="token punctuation">.</span>append<span class="token punctuation">(</span>Klasse<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">.</span>add<span class="token punctuation">(</span><span class="token string">"Laura"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>add<span class="token punctuation">(</span><span class="token string">"Lucas"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>add<span class="token punctuation">(</span><span class="token string">"Matthias"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>add<span class="token punctuation">(</span><span class="token string">"Marcus"</span><span class="token punctuation">)</span><span class="token punctuation">)</span>
skole<span class="token punctuation">.</span>klasser<span class="token punctuation">.</span>append<span class="token punctuation">(</span>Klasse<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">.</span>add<span class="token punctuation">(</span><span class="token string">"William"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>add<span class="token punctuation">(</span><span class="token string">"David"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>add<span class="token punctuation">(</span><span class="token string">"Asta"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>add<span class="token punctuation">(</span><span class="token string">"Sofie"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>add<span class="token punctuation">(</span><span class="token string">"Albert"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>add<span class="token punctuation">(</span><span class="token string">"Karla"</span><span class="token punctuation">)</span><span class="token punctuation">)</span>
</code></pre>
<h2 id="integrering-af-builder-pattern-i-appen">Integrering af Builder Pattern i Appen</h2>
<p>Her er et udklip af en klasse fra mit program, der bruger Builder Pattern:</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">class</span> <span class="token class-name">Equation</span><span class="token punctuation">:</span>
    <span class="token keyword">def</span> <span class="token function">__init__</span><span class="token punctuation">(</span>self<span class="token punctuation">,</span> operation <span class="token operator">=</span> <span class="token string">""</span><span class="token punctuation">,</span> value <span class="token operator">=</span> <span class="token string">""</span><span class="token punctuation">,</span> parent <span class="token operator">=</span> <span class="token boolean">None</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
        self<span class="token punctuation">.</span>operation <span class="token operator">=</span> operation
        self<span class="token punctuation">.</span>children <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token punctuation">]</span>
        self<span class="token punctuation">.</span>value <span class="token operator">=</span> value
        self<span class="token punctuation">.</span>parent <span class="token operator">=</span> parent

    <span class="token comment"># The method for adding a sub equation the the equation.</span>
    <span class="token keyword">def</span> <span class="token function">Add</span><span class="token punctuation">(</span>self<span class="token punctuation">,</span> operation <span class="token operator">=</span> <span class="token string">""</span><span class="token punctuation">,</span> value <span class="token operator">=</span> <span class="token string">""</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
        
        <span class="token comment"># If the new equation is a lone number, use the AddNum Method for adding a number equation.</span>
        <span class="token keyword">if</span> <span class="token builtin">isinstance</span><span class="token punctuation">(</span>operation<span class="token punctuation">,</span> <span class="token punctuation">(</span><span class="token builtin">float</span><span class="token punctuation">,</span> <span class="token builtin">int</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
            self<span class="token punctuation">.</span>AddNum<span class="token punctuation">(</span>operation<span class="token punctuation">)</span>

            <span class="token comment"># The Builder pattern returns self so I can chain methods:</span>
            <span class="token keyword">return</span> self
        
        <span class="token comment"># Else, just at the info from the constructor to children as a sub equation.</span>
        self<span class="token punctuation">.</span>children<span class="token punctuation">.</span>append<span class="token punctuation">(</span>Equation<span class="token punctuation">(</span>operation<span class="token punctuation">,</span>value<span class="token punctuation">,</span>self<span class="token punctuation">)</span><span class="token punctuation">)</span>

        <span class="token comment"># This isn't classical Builder Pattern, since I'm diving a level. Here, I just added a shortcut to make things easier here in building.</span>
        <span class="token keyword">return</span> self<span class="token punctuation">.</span>children<span class="token punctuation">[</span><span class="token builtin">len</span><span class="token punctuation">(</span>self<span class="token punctuation">.</span>children<span class="token punctuation">)</span><span class="token operator">-</span><span class="token number">1</span><span class="token punctuation">]</span>

    <span class="token keyword">def</span> <span class="token function">AddNum</span><span class="token punctuation">(</span>self<span class="token punctuation">,</span> num<span class="token punctuation">)</span><span class="token punctuation">:</span>
        self<span class="token punctuation">.</span>children<span class="token punctuation">.</span>append<span class="token punctuation">(</span>Equation<span class="token punctuation">(</span><span class="token string">""</span><span class="token punctuation">,</span><span class="token builtin">str</span><span class="token punctuation">(</span>num<span class="token punctuation">)</span><span class="token punctuation">,</span>self<span class="token punctuation">)</span><span class="token punctuation">)</span>

        <span class="token comment"># The Builder pattern returns self so I can chain methods:</span>
        <span class="token keyword">return</span> self
</code></pre>
<p>Og her vises den udnyttet i programmet:</p>
<pre class=" language-python"><code class="prism  language-python">first_dict <span class="token operator">=</span> <span class="token punctuation">{</span>
    <span class="token number">1</span><span class="token punctuation">:</span> Equation<span class="token punctuation">(</span><span class="token string">"+"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">2</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">2</span><span class="token punctuation">)</span><span class="token punctuation">,</span>    
    <span class="token number">2</span><span class="token punctuation">:</span> Equation<span class="token punctuation">(</span><span class="token string">"+"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">5</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">7</span><span class="token punctuation">)</span><span class="token punctuation">,</span>    
    <span class="token number">3</span><span class="token punctuation">:</span> Equation<span class="token punctuation">(</span><span class="token string">"-"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">8</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">3</span><span class="token punctuation">)</span><span class="token punctuation">,</span>    
    <span class="token number">4</span><span class="token punctuation">:</span> Equation<span class="token punctuation">(</span><span class="token string">"+"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">4</span><span class="token punctuation">)</span><span class="token punctuation">,</span>    
    <span class="token number">5</span><span class="token punctuation">:</span> Equation<span class="token punctuation">(</span><span class="token string">"-"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">6</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">2</span><span class="token punctuation">)</span><span class="token punctuation">,</span>    
    <span class="token number">6</span><span class="token punctuation">:</span> Equation<span class="token punctuation">(</span><span class="token string">"+"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">3</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">3</span><span class="token punctuation">)</span><span class="token punctuation">,</span>    
    <span class="token number">7</span><span class="token punctuation">:</span> Equation<span class="token punctuation">(</span><span class="token string">"-"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">9</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">4</span><span class="token punctuation">)</span><span class="token punctuation">,</span>    
    <span class="token number">8</span><span class="token punctuation">:</span> Equation<span class="token punctuation">(</span><span class="token string">"+"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">2</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">6</span><span class="token punctuation">)</span><span class="token punctuation">,</span>    
    <span class="token number">9</span><span class="token punctuation">:</span> Equation<span class="token punctuation">(</span><span class="token string">"-"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">7</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">,</span>    
    <span class="token number">10</span><span class="token punctuation">:</span> Equation<span class="token punctuation">(</span><span class="token string">"+"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">4</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">5</span><span class="token punctuation">)</span><span class="token punctuation">,</span>   
    <span class="token number">11</span><span class="token punctuation">:</span> Equation<span class="token punctuation">(</span><span class="token string">"-"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">10</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">3</span><span class="token punctuation">)</span><span class="token punctuation">,</span>  
    <span class="token number">12</span><span class="token punctuation">:</span> Equation<span class="token punctuation">(</span><span class="token string">"+"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">9</span><span class="token punctuation">)</span><span class="token punctuation">,</span>   
    <span class="token number">13</span><span class="token punctuation">:</span> Equation<span class="token punctuation">(</span><span class="token string">"-"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">5</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">2</span><span class="token punctuation">)</span><span class="token punctuation">,</span>   
    <span class="token number">14</span><span class="token punctuation">:</span> Equation<span class="token punctuation">(</span><span class="token string">"+"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">6</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">,</span>   
    <span class="token number">15</span><span class="token punctuation">:</span> Equation<span class="token punctuation">(</span><span class="token string">"-"</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">8</span><span class="token punctuation">)</span><span class="token punctuation">.</span>Add<span class="token punctuation">(</span><span class="token number">5</span><span class="token punctuation">)</span>    
<span class="token punctuation">}</span>
</code></pre>
<h2 id="udviklingsprocessen">Udviklingsprocessen</h2>
<p>Jeg startede med at researche omkring forskellige design patterns, men valgte ikke et før, jeg vidste, hvad jeg ville arbejde med.<br>
Efter at have fundet ud af det, brugte jeg mit design pattern til at skrive en masse regnestykker, som brugerne kan løse. Dette har jeg brugt Builder Pattern til.</p>
<h2 id="brugergrænsefladen">Brugergrænsefladen</h2>
<p>Brugergrænsefladen er meget simpel, da jeg hovedsageligt fokuserede på at lave noget udfordrende. Da jeg godt ved, hvordan man bruger Tkinter i forvejen, kunne jeg godt holde lidt tilbage med det.</p>
<h3 id="brugergrænsefladen-har-blot-4-elementer">Brugergrænsefladen har blot 4 elementer</h3>
<ol>
<li><strong>Equation Label:</strong> Her bliver regnestykkerne vist for brugerne.</li>
<li><strong>Input Field:</strong> Her kan brugeren skrive sit svar ind.</li>
<li><strong>Submit Button:</strong> Brugeren kan trykke på denne for at få sit svar valideret.</li>
<li><strong>Result Text:</strong> Denne tekst giver resultatet for brugerens svar.</li>
</ol>
<h2 id="test-af-programmet">Test af programmet</h2>

<table>
<thead>
<tr>
<th>Hvad Testes?</th>
<th>Forventet Resultat</th>
<th>Faktisk Resultat</th>
</tr>
</thead>
<tbody>
<tr>
<td>Input af korrekt svar</td>
<td>“Correct!”</td>
<td>“Correct!”</td>
</tr>
<tr>
<td>Input af forkert svar</td>
<td>“Not Correct :C”</td>
<td>“Not Correct :C”</td>
</tr>
<tr>
<td>Input af intet svar</td>
<td>“Not Correct :C”</td>
<td>“Not Correct :C”</td>
</tr>
<tr>
<td>Input af bogstaver</td>
<td>“Not Correct :C”</td>
<td>“Not Correct :C”</td>
</tr>
<tr>
<td>Spamming “Submit”</td>
<td>“Not Correct :C”</td>
<td>“Not Correct :C”</td>
</tr>
</tbody>
</table></div>
</body>

</html>
