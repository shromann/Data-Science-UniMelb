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
1. English Auction: Ascending bid
2. Dutch Auction: Descending bid
3. First-priced sealed bid auction: One-Shot Bid
4. Vicerey Auction: Second Price bidding
