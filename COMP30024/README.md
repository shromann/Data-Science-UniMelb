# COMP30024 Artificial Intelligence
> by Shromann Majumder 

#  Intelligent Agent
- **Agent model** characterize requirements for an agent in terms of its percepts, actions, environment and performance measure
- **Agent types** choose and justify choice of agent type for a given problem
- **Environment types** characterize the environment for a given problem

## Outline

- Defining AI
- Tests for intelligence
- State of the art
- Agent model
- Agent types
- Environment types

# Solving By Search

Problem  formulation  usually  requires  abstracting  away  real-world  details  to define a state space that can feasibly be explored
Variety of uninformed search strategies. 
**Iterative deepening** search uses only linear space and not much more time than other uninformed algorithms

## Outline
- Problem-solving agents
- Problem types
- Problem formulation
- Example problems
- Basic search algorithms

## Expectations
1. Formulate single-state search problem 
2. Apply a search strategy to solve problem
3. Analyse complexity of a search strategy

# Informed Search

Heuristics help reduce search cost, however, finding an optimal solution is still difficult. 

- **Greedy best-first search** is not optimal, but can be efficient.
- **A\* search** is complete and optimal, but is prohibitive in memory.
- **Hill-climbing** methods operate on complete-state formulations,require less memory, but are not optimal.

## Outline

- Best-first search
- A∗search
- Heuristics
- Hill-climbing

## Expectations
1. Demonstrate operation of search algorithms
2. Discuss and evaluate the properties of search algorithms
3. Derive and compare heuristics for a problem

#  Game Playing & Adversarial Search

Games illustrate several important points about AI

- perfection is unattainable⇒must approximate and make trade-offs
- uncertainty limits the value of look-ahead
- can programs learn for themselves as they play?  (cont. ML for Game Playing)

## Outline

- Perfect play
- Resource limits
- $α–β$ pruning
- Games of chance

## Expectations
1. Demonstrate operation of game search algorithms
2. Discuss and evaluate the properties of game search algorithms
3. Design suitable evaluation functions for a gam
4. Explain how to search in nondeterministic games

#  Machine Learning for Game Playing
Many design decisions need to be fine-tuned in game playing agents Can we automatically tune these decisions?

## Outline 
- Supervised learning using **gradient decent search**
  - **Delayed  reinforcement**:   reward  resulting  from  an  action  may  not  be  received until several time steps later, which also slows down the learning
  - **Credit assignment**:  need to know which action(s) was responsible for the outcome
- **Temporal difference** learning in games
- **Book learning**: learn sequence of moves for important positions
- **Search control learning**: learn how to make search more efficient
- **Learning evaluation function weights**: adjust weights in evaluation function based on experience of their ability to predict the true final utility 

## Expectation
1. Discuss opportunities for learning in game playing
2. Explain differences between supervised and temporal difference learning
3. I do not expect you to derive or memories the TDLeaf(λ) weight update rule,  but  if  given  this  rule  I  may  ask  you  to  explain  what  the  main  terms mean


#  Constraint Satisfaction Problem

CSPs are a special kind of problem:
- states defined by values of a fixed set of variables
- goal test defined by constraints on variable values
  
## Summary
1. **Backtracking**: depth-first search with one variable assigned per node
2. **Variable ordering** and **value selection** *heuristics* help significantly 
3. Forward checking prevents assignments that guarantee later failure
4. Constraint propagation (e.g., arc consistency) does additional work to constrain values and detect inconsistencies
5. The CSP representation allows analysis of problem structure
6. Tree-structured CSPs can be solved in linear time
7. Iterative min-conflicts is usually effective in practice

## Outline
 - CSP examples
 - **Backtracking search** for CSPs
 - Problem structure and problem decomposition
 - Local search for CSPs

## Expectation
 1. Model a given problem as a CSP
 2. Demonstrate operation of CSP search algorithms
3. Discuss and evaluate the properties of different constraint satisfaction techniques

#  Complex Decisions - Auctions
Auctions are a mechanism to allocate resources in multi-agent environments
Appropriate mechanism design can achieve desirable behavior
among selfish agentsTypes of auctions in theoryPractical case studies of on-line auctions

## Outline 
 - Mechanism design for allocating scarce resources
 - Properties of auctions
 - Types of auctions
 - On-line auctions in practice

## Expectation 
1. Compare and contrast different types of auctions
2. Describe the properties of a given type of auction
3. Select the most appropriate type of auction for a given application

#  Uncertainty
Probability is a rigorous formalism for uncertain knowledgeJoint probability distribution specifies probability of every atomic eventQueries can be answered by summing over atomic eventsFor nontrivial domains, we must find a way to reduce the joint sizeIndependence and conditional independence provide the tools

## Outline
 - Uncertainty
 - Probability
 - Syntax and Semantics
 - Inference
 - Independence and Bayes’ Rule

## Expectation
1. Calculate conditional probabilities using inference by enumeration
2. Use conditional independence to simplify probability calculations
3. Use Bayes’ rule for solving diagnostic problems

#  Bayesian Belief System
Bayes nets provide a natural representation for (causally induced)conditional independence
Topology + CPTs = compact representation of joint distribution
Generally easy for (non)experts to constructExact inference by enumeration
Exact inference by variable elimination

## Outline 
 - Syntax
 - Semantics
 - Exact inference by enumeration
 - Exact inference by variable elimination

## Expectation
 1. Formulate a belief network for a given problem domain
 2. Derive expression for joint probability distribution for given belief network
 3. Use inference by enumeration to answer a query about simple or conjunctive queries on a given belief network

#  Robotics

## Outline
- Robots, Effectors,and Sensors 
- Localization and Mapping 
- Motion Planning

## Expectation
 1. Percepts and actions are both subject to uncertainty.
 2. We cannotinterpretourperceptswithouthavinga model of what they mean,and without(partially invalid)assumptions about how they perform.
 3. Uncertainty in robot perception.
 4. Incremental form of Bayes Law.
 5. Motion planning.











