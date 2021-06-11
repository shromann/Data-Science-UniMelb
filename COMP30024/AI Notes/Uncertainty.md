# Uncertainty
> Relevant when there are issues around the agent; such as *partial observability*, *noisy sensors*, *uncertainty in action outcomes*
### Handling Uncertainty

1. **Non-monotonic logic**:
   1. What assumptions are made?
   2. What assumptions are reasonable
2. **Rules w/ confidence factors**:
   1. $A_{25} \mapsto 0.3$ get on time
   2. sprinkler $\mapsto 0.3$ wet grass
   3. Essential map an event to an outcome with its confidence.
   4. Problematic when multiple combinations happen
3. **Probability**: (Focus in this course)
   - given some information, I can tell that this event will map to ths with *probability* of $x$
4. **Fuzzy Logic**:
   - handles degrees of truths

## Probability
> Quantifies everything we can't predict
- Probabilistic assertion summarize effects of:
    1. **laziness**: not being able to consider all exceptions, qualifications...
    2. **ignorance**: lack of relevant facts

- Subjective vs **Bayesian**:
  - What is the probability of something happening, knowing that something else happened too?
  $$P(A_{25}|\text{no reported accidents})$$
  - Modelling the *uncertainty* in our beliefs, rather than the uncertainty in the world.  
  $$P(A_{25}|\text{no reported accidents, 5am})$$

  - So how do we choose the best action??
    - Depends on preference.
    - Utility Theory
      1. Represent preference
      2. Inference preference
    - Decision Theory
      - utility theory + probability theory

## Syntax & Semantics
> Already did this stuff in `Probability` and `Models of Computation`
### Probability
  - Sample Space: $\Omega$
  - event: $\omega$
  - Probability Space: $P(\omega) :  \omega \in \Omega$
  - Random Variable: $\omega \rightarrow \mathbf{Range}$ ($\mathbb{R}$, Booleans)
  - $P$ induces a **Probability Distribution** for any r.v $X$: $P(X = x_1)$
### Propositions
  - The event where the proposition is true. (like $\omega$)
  - event $a \implies A(\omega) = \text{true}$ 
  - event $\neg a \implies A(\omega) = \text{false}$ 
  - event $a \land b  \implies A(\omega) = \text{true } \text{and } B(\omega) = \text{true}$ 
  - Describing Events
    - **Propositional** (boolean): $Cavity$ (do I have cavity or not?)
    - **Discrete** r.v (finite or infinite): $Weather \in \{sunny, rain, cloudy, snow\}$
    - **Continuous** r.v (bounded or unbounded): $Temp = 21.6$ or $Temp < 22.0$

#### So why use **Probability**?
- The definitions show that some logically related events must have related probabilities
- for e.g: $P(a \land b) = P(a) + P(b) - P(a \lor b)$ (**related!**)
- will lose if an agent violates these related probabilities. 

### Prior Probability
1. **Prior Probability** (unconditional): the probability of something without knowing anything
2. **Probability distribution** gives values for all possible assignments
3. **Joint probability distribution** for a set of r.v.s gives of every possible combination of events. 
   
### Posterior Probability
1. **Posterior Probability** (conditional): the probability of something after updating knowledge.
   $P(a | b) = \frac{P(a \land b)}{P(b)} = \frac{P(b | a)P(a)}{P(b)}$
2. **Product Rule**: $P(a \land b) = P(a | b)P(b) = P(b|a)P(a)$
3. **Chain Rule**: $P(X_1, ... X_n) = P(X_1, ..., X_{n-1}) P(X_n | X_1, ..., X_n)$

## Inference by Enumeration
- **Normalization**
  - In *Conditional* probability, express the denominator as a constant.
  - $P(c|t) = \alpha\ P(c,t) = \alpha\ [P(c,t, \neg I) + P(c,t, I)]$
> Interested in **posterior** join distribution of the query Y given E, where hidden variables are H = X - Y - E
- $P(Y|E=e) = \alpha P(Y,E=e) = \alpha \sum_{h}P(Y, E = e, H = h)$
- Time: $O(d^n)$
- Space: $O(d^n)$
- How to find numbers for $O(d^n)$ entries??
  - INDEPENDENCE

## Independence
1. Independence 
   - $P(A|B) = P(A)$
   - $P(B|A) = P(B)$
   - $P(A,B) = P(A)P(B)$
   - Absolute Independence is powerful but **rare**. 
2. Conditional Independence
   - $P(catch|toothache, cavity) = P(catch|cavity)$
   - $P(catch|toothache, \neg cavity) = P(catch|\neg cavity)$
   - $P(Catch|Toothache, Cavity) = P(Catch|\neg Cavity)$ (the class)
   - $P(Toothache|Catch, Cavity) = P(Toothache|Cavity)$
   - $P(Toothache, Catch | Cavity) = P(Toothache|Cavity)P(Catch|Cavity)$
   - This means we can use reduce the follow:
     - $P(X, Y, Z) = P(X| Y, Z)P(Y, Z) = P(X | Y)P(X | Z)P(Y, Z)$

## Bayes Rule
> Useful for understanding `cause` and `effect`
- $P(Cause|Effect) = \frac{P(Effect|Cause)P(Cause)}{P(Effect)} = \alpha P(Effect|Cause)P(Cause)$
 