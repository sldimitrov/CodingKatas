# Learn through PRACTICE
## KATAS

### KATA #1: Supermarket Pricing

---

#### 1. Pricing Models

- Price per 1 item
- Price per (x) quantity — _Does the item have price?_
- Price per pound — _So what do 4 ounces cost?_
- Buy two get three — _So does the third item have a price?_


| id | price | pack_price | pound_price | is_one_free | stock_id |
|----|-------|------------|-------------|-------------|----------|
| 1  | 0.60  | 1.50       | x           | TRUE        | 555      |

> This database represents the prices array and with this the **pricing schema**.

---

### 2. Audit Trail of Pricing

_We could keep an audit trail of pricing decisions_

#### Reasons:

- **Transparency & Accountability**
- **Risk Management**
- **Process Improvement**
- **Data-driven Decision Making**

#### Tradeoffs:

- **Increased Complexity**

#### How To:

**I.** Store a list with previous price changes within the product  
→ _Too many properties_

**II.** Create separate table with logs for each `product_id`, storing their pricing log  
→ _Separation of Concerns ✅_

---

### 3. Cost VS Price

#### Option 1

Cost and price could be represented with the same entity, but there should be a `type` property to differentiate them:

```plaintext
+------------+--------+-------+
| product_id | type   | price |
+------------+--------+-------+
|     5      | cost   | 0.50  |
|     5      | price  | 0.65  |
+------------+--------+-------+
