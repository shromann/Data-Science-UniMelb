All Materials Available in [COMP30024](https://github.com/shromann/Data-Science-UniMelb/blob/main/COMP30024/). For **Exam Prep**, suss out [Course Outline & Expectations](https://github.com/shromann/Data-Science-UniMelb/blob/main/COMP30024/README.md)

# Complex Decisions      
## Mechanism Design
> The problem of how to design a "game" that maximizes a global utility function in a multi-agent system, given each agent goes for their own strategy

-  In AI, the aim is to make smart systems out of simpler systems to do things beyond simple single system. 

- This subject only deals with *Auctions*

###  Types of Mechanism Design problems
1. **Single Item Auctions**: standard auction where person $i$ values the sale item at $v_i$ and private to $i$. Now how do we design the rules get equilibrium outcome that is good for the *auctioneer* and *bidders*.
2. **Combinatorial Auctions**: generalizing single item auction to a set $T$ of $m$ items. Utility : $v_i:2^T \rightarrow \mathbb{R}$. Goal is to partition $T$ to $S_1, S_2, S_3,..., S_n$ and maximite $\sum_{i=1}^{n}v_i(S)$
3. **Public Projects**: same a single item auction tbh, I couldn't tell the difference lmao
4. **Voting**: $n$ player; $m$ candidates. all players put preference down for all m candidates. Like how our new uni timetabling preference is like aha.

## Auctions 
> We focus on **mechanism design** for **auctions**. So what even is an Auction?
   - **Bidder**: *Maximizing Price*
      - Maximum budget
      - How much do I even value it?
   - **Auctioneer**: *Maximizing Price*
      - Fake bidding to push the price

A mechanism for an auction consists of
1. a **language** to describe strategies an agent can follow
2. a **protocol** for bids from bidders to auctioneer
3. an **outcome rule**, used by auctioneer

### Dimensions of auction protocols
- **Winner Determination**: which bidder wins and what do they pay?
   1. **First Price** auctions: bidder with the highest big is allocated the good
   2. **Second Price** auctions: bidder with the highest big is allocated the good but paying the *second* highest price.
- **Knowledge of bids**: who can see this?
    1. **Open-cry**: everyone can see it
    2. **Sealed-bid**: **Only** bidder and auctioneer can see, no one else can see.
- **Order of bids**: what order are the bids made?
  1. **One-Shot**: each bidder can make only one bid
  2. **Ascending**: last bid < curr bid
  3. **Descending**: last bid > curr bid
- **# of Goods**: How many goods are for sale?
     1. **Single Good**: only one indivisible good for sale (We **focus** on this)
     2. Many Goods: many goods are available for sale (*Combinatorial Auction*)

### Factors affecting Mechanism Design
1. Common value: The worth of the item is the **same** for all bidder
2. Private Value: The worth of the item is the **different** for all bidder

### Desirable Properties of an **auction**
- **Efficient**: go to the person who *values* it the most
- **Discourage Collusion**: no illegal arrangements to make the game biased
- **Dominant Strategy**: there is a *dominant* strategy $\iff$ if this strategy gives a better pay-off than other strategies.
- **Truth-Revealing**: The dominant strategy results in bidders revealing their true value for the good. 

### Relation to **AI**
- Modern On-Line auctions require agents who can bid good
- Agents model user's preference for their strategy
- These agents need a representation language for bids

### Types of Auctions
1. **English Auction**
   - ascending
   - first-price
   - open-cry
   - kinda waiting for bids. 
   - **Dominant Strategy**: keep bidding in small bids until cost < value
   - **Properties**:
     - **efficient**: Good auction unless the starting bid is too high (bad for bidder), or too low (bad for auctioneer). 
     - may occur **winner's curse**: paying too much, a lot above other bidders value rather than just a bit up and enough to win.
     - *susceptible* to **Collusion**:
       - *bidder* can agree beforehand to keep bids artificially low
       - *auctioneers* can plant "dummy" bidders to raise prices. 
2. **Dutch Auction:**
   - descending
   - open-cry
   - good for a fast paced auction
   - auctioneer start with a VERY HIGH PRICE, then slowly lowers the price. It ends when someone pays at the current price. Here the auctioneer is changing the price, and bidder just wait and choose. 
   - **Properties**:
     - **efficient**: Amazing for auctioneer but bad for bidder cause more likely for winners curse. 
     - **winner's curse**: paying too much, a lot above other bidders value rather than just a bit up and enough to win.
     - *susceptible* to **Collusion**:
       - *bidder* can agree beforehand to keep bids artificially low
       - *auctioneers* can plant "dummy" bidders to raise prices. 
3. **First-priced sealed bid auction**
   - each bidder bids **only** once.
   - sent to auctioneer without sharing.
   - sealed-bid
   - price paid by winner with the highest bid
   - **Dominant Strategy**: don't know, but be true to yourself and bid less than your true value. might result in a bit of winners curse if your value is higher than others.
   - used for *governments contracts*
   - **Properties**:
     - **not efficient**: since agent with the highest value may lose.
     - **winner's curse**: paying too much, a lot above other bidders value rather than just a bit up and enough to win.
     - ***not susceptible*** to **Collusion**:
       - *bidder* can't see shit 
4. **Vicerey Auction: Second Price bidding**
   - second-price
   - sealed-bid
   - winner pays the price with the second highest price.
   - **Dominant Strategy**: go straight for the value, going over it might lead to winners curse if the second highest is also above the value. But going your bid, will deffs not be winners curse due cause your bid acts as a bound. 
   - **Properties**:
     - **efficient** & **truth-revealing**: since dominant strategy is to bid your value.
     - **NO** **winner's curse**: Due to bounds
     - harder to **Collusion**: *bidder* can't see shit cause its sealed
     - computational simplicity makes it popular for use in multi-agent AI systems and on-line auctions.