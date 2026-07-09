---
type: Sales Table
title: Orders
description: Uma linha por pedido confirmado.
resource: https://example.com/data/orders
tags: [sales, orders]
timestamp: 2026-07-09T00:00:00Z
---

# Schema

| Column | Type | Description |
|---|---|---|
| `order_id` | STRING | Identificador do pedido |
| `customer_id` | STRING | Referencia para [customers](./customers.md) |

# Citations

- [Dataset de exemplo](https://example.com/data/orders)