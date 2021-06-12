# Linear Algebra 
## Basics
### Matrix & Manipulation 
1. Partitioning: we can partition matrices and treat **sub-matrices** like numbers
2. Transposition: Replacing rows with columns in a matrix
   - $(XY)^T = Y^TX^T \neq X^T Y^T$
   - symmetric $\iff X^T = X$
1. Identity: Square matrix where 1's across the diagonal and 0's everywhere else. $(A_k)$
2. Inverse: X is square $\iff XX^{-1} = X^{-1}X = I$
   - may **not always exist**
   - if it does, then X is **nonsingular**
   - X is **singular** $\iff$ $|X| = 0$ (determinant)

### Orthogonality
$$\mathbf{x}\perp\mathbf{y}  \iff \mathbf{x}^T\mathbf{y}=\sum_{i=1}^{n}x_i y_i = 0$$
- $X \perp \iff X^TX = I$
- $X \perp \implies X^{-1} = X^T$
- *norm* of x: Square root of $\mathbf{x} = ||\mathbf{x}||$ 

### Eigenthings
$$A\mathbf{x} = \lambda \mathbf{x}$$ 
- To find eigenvalues, solve $|A - \lambda I| = 0$
- To find eigenvectors, sub in eigenvalues and solve for $\mathbf{x}$
- **Properties**
  1. A is **real** and **symmetric** $\implies$ eigenvalues $\in \mathbb{R}$ and eigenvectors are orthogonal.
  2. P is orthogonal matrix (Square, same size as A) $\implies$ $P^T A P$ and $A$ have the same eigenvalues ($P$ **diagonalizes** $A$)

### Rank
- Linear Independence: when the vectors cannot be expressed as a linear combination of other vectors.
- Rank: the number of linearly independent (column) vectors
  - $r(X) = r(X^T) = r(X^TX)$
  - $X: k \times k \implies$$X^{-1}$ exists $\iff r(X) = k$
  - $X: n \times k \land ( Q:k \times k \land \text{nonsingular} ) \land ( P:n \times n \land \text{nonsingular} )\implies r(X) = r(PX) = r(XQ)$
- $r(\text{diagonal matrix}) =$ # of non-zero entires.
- $r(XY) \leq r(X), r(Y)$

### Idempotent
$$A^2 = A$$
- To show impotence, just times it by it self and reduce it down to the original statement

### Trace
$$tr(X) = \sum_{i=1}^{k}x_{ii}$$
- Sum of the diagonals
- **Properties**
  1. $tr(c\times X) = c\times tr(X)$
  2. $tr(X \plusmn Y) = tr(X) \plusmn tr(Y)$
  3. $XY \land YX$ both exist $\implies tr(XY) = tr(YX)$

## Theorems
### Symmetric & Impotence Theorems 
1. The eigenvalues of idempotent matrices are always either 0 or 1.
2. if A is a symmetric and idempotent, $r(A) = tr(A)$.
3. Let A1, A2, . . . , Am be a collection of symmetric k × k matrices. Then the following are equivalent:
   - There exists an orthogonal matrix P such that PTAiP is diagonal for all i = 1,2,...,m;
   - AiAj = AjAi for every pair i,j = 1,2,...,m.
4. Let A1, A2, . . . , Am be a collection of symmetric k × k matrices. Then any two of the following conditions implies the third:
   -  All Ai, i = 1,2,...,m are idempotent; 
   -  $\sum_{i=1}^{m}A_i$ is idempotent;
   -  Ai Aj = 0 for i $\neq$ j.
5. Let A1, A2, . . . , Am be a collection of symmetric k × k matrices. If the conditions in Theorem 2.5 are true, then 
$$r\left( \sum_{i=1}^{m}A_i \right) = \sum_{i=1}^{m}r(A_i)$$

### Positive Definite Theorems
6. A symmetric matrix A is positive definite if and only if its eigenvalues are all (strictly) positive.
7. A symmetric matrix A is positive semi-definite if and only if its eigenvalues are all non-negative.


## Quadratic Forms
$$q = \mathbf{y}^T A \mathbf{y} = \sum_{i=1}^{k}\sum_{j=1}^{k}a_{ij}y_{i}y_{j}$$
- $q$: is a *quadratic form* in y
- $A$: the matrix of the *quadratic form*

### Positive Definiteness
- **Positive Definite**: $q > 0\ |\ \forall \mathbf{y} \neq \mathbf{0}$ 
  - kinda like when a parabola is always above the x axis
-  **Positive Semi-Definite**: $q \geq 0\ |\ \forall \mathbf{y}$

### Differentiation of Quadratic Forms
$$\frac{\partial z}{\partial \mathbf{y}} = \begin{bmatrix} \partial z/\partial y_1 \\ \partial z/\partial y_2 \\ \vdots \\ \partial z/\partial y_k\\  \end{bmatrix} $$

- Just do the partial derivative w.r.t each variable in the vector $\mathbf{y}$
- **Properties**
  - $z = \mathbf{a}^T\mathbf{y} \implies \frac{\partial z}{\partial \mathbf{y}} = \mathbf{a}$ ($a$ is constant)
  - $z = \mathbf{y}^T\mathbf{y} \implies \frac{\partial z}{\partial \mathbf{y}} = 2\mathbf{y}$
  - $z = \mathbf{y}^TA\mathbf{y} \implies \frac{\partial z}{\partial \mathbf{y}} = A\mathbf{y} + A^T\mathbf{y}$
    - $A$ is symmetric $\implies \frac{\partial z}{\partial \mathbf{y}} = 2A\mathbf{y}$
  

# Random Vectors


> Questions:
> 1. How does **diagonalisation** work?
> 2. What does an orthogonal matrix mean?
> 3. why are eigenvectors are orthogonal for a real and symmetric matrix A?
> 4. Fuck the theorems aren't clicking (yet aha) 