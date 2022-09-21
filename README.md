### Calculations
#### Target ratio

$$
ratio_i = \frac{budget_i}{\sum_{k=1}^n budget_k}
$$

#### Actual ratio

$$
ratio_i = \begin{cases}
\frac{views_i}{\sum_{k=1}^n views_k} & \text{if } \sum > 0, \\
0 & \text{otherwise}
\end{cases}
$$

#### Error

$$
error(actual, target) = \begin{cases}
target - actual & \text{if } actual < target, \\
\frac{actual - target}{target} & \text{otherwise}
\end{cases}
$$

#### Next view

Next view goes to an advertiser who has minimum value (best error reduction)

$$
delta_i = error(\frac{views_i}{total\_views + 1}, target_i) - error(\frac{views_i + 1}{total\_views + 1}, target_i) \text{,} \\ \text{where }total\_views = \sum_{k=1}^n views_k
$$

### Issues

#### User location

An advertiser budget can be reduced based on proximity.

For example, the advertiser wants to spend less than 40% of budget for users from 5 to 10 kilometers far from the shop and spend nothing for more distant users.

#### Limited number of products in a shop

An advertiser risks to get less views if its shop contains few products and there are only unique products in the advertisement block.

#### Views disproportion

1. It's not guaranted that an advertiser gets enouth or even any user visit for his requirements.

2. Sometimes all advertiser candidates have enough views. We should add them views anyway or hide the advertisement block.

3. The least budgets can get no views
