# Which search?

> Three ways to find a value, and how to tell from the statement which one a problem asks for; after it, the learner
> names the search before writing a line.

**Shape:** [recognition guide](../recognition-guide.md).

## Types

- **T1** Binary search: a sorted sequence, or a yes-or-no question that turns from no to yes once.
- **T2** Linear scan: one pass over values in no order.
- **T3** Lookup in a table: many exact-match queries against the same set.

## Signals

| Type | In the statement | In the model | Tool | Not when |
|---|---|---|---|---|
| T1 | "sorted", "the first position where", "the smallest k such that" | a predicate monotone in the index: false up to a point, true after | halve the interval, O(log n) | the order is on another key than the one searched |
| T2 | "unsorted", "once", "the maximum of" | every element can decide alone | one pass, O(n) | the same list is searched again and again |
| T3 | "is x in the set", "for each query", "lookup" | equality only, no order needed | a hash table, O(1) per query after O(n) | the query asks for the nearest value, not an equal one |

## Decision

1. Is the question an exact match asked many times on one set? Yes: T3. No: next.
2. Is there an order, or a yes-or-no that flips once along the index? Yes: T1. No: T2.

## Not one of them

| Looks like | Why not | What it is |
|---|---|---|
| "sorted by date, find the largest amount" | the order is on the date, the question is on the amount: the predicate does not flip once | T2, a scan |
| "nearest value to x in a sorted list" | binary search finds where x would go; the nearest is one of its two neighbours | T1, then one comparison |
| "two numbers that sum to x" | one index is not enough; sorting first gives two pointers, a table gives T3 per element | neither alone |

## Check yourself

1. A log of timestamps in increasing order; find the first entry after midnight.
   <details><summary>Answer</summary> T1: the order is on the timestamp and "first after" flips once, from before to after. </details>
2. A list of 10 000 words; for each of 1 000 000 sentences, say whether its words are all in the list.
   <details><summary>Answer</summary> T3: exact matches, many queries, one set; build the table once. </details>
3. A checker says whether k trucks can carry all the parcels. Find the smallest k.
   <details><summary>Answer</summary> T1 without an array: "k trucks suffice" is false then true once as k grows, so halve on k. </details>

## See also

The [lesson](binary-search-lesson.md) that teaches T1, the [sheet](binary-search-sheet.md) that drills it, and the
[guide](binary-search-guide.md) that revises it; [examples](README.md), the folder this one sits in.
