# FaisalBhaiAi

<b>This is my logfile I will use it to show what I am working on and my thought process.</b> 

>21/2/2021
1.  using networkx library for graphing. using the edmond karp (EK) max flow algorithm to 
    find out the best case allocation.
    however there is a problem
    a.  when case gets allocated to one arbitrator e(case, arb) = p(case accepted by arb) < 1.
        But e(arb, t) = 1 if flow(case, arb) > 0. In that case, EK algorithm fails.
    b.  Solution? have another data structure and make a fix for this.

2.  next step?
    1.  think about modified EK algorithm   <-- harder, fun
    2.  make AI model   <-- easier, boring

>23/02/2021:
1.  decided to make the AI model as modifing EK algorithm will take a long time and making 
    AI model is more beneficial.
2.  made the data for the model

>24/02/2021:
1.  making the preprocessing bit.
2.  there is such a thing as categorical embeddings. Use it for Arbitrator_bg and Case_nature 
    later. For now I will use simple one-hot encoding.
    
    
>25/02/2021:
1.  Need to git push everyday
2.  continue making preprocessing bit.
3.  Just learnt of new activation function - swish. Can do tests (later) to check if it increases accuracy.
    Will use ReLU for now.
4.  Finishing work for today. Made a test.ipynb which has the rough work. Ive made simple NN model with 2 hidden layers 
    (100, 50). Need to make training, validation, testing loops.
    