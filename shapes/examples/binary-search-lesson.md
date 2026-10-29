# Binary search

> Binary search finds a value in an ordered list by halving the part that can still hold it. It needs about log2 n
> comparisons, where a scan of the list needs n.

**Shape:** [lesson](../lesson.md).

## Objectives

- **O1** Trace binary search step by step, writing the bounds `lo` and `hi` after each comparison.
- **O2** Explain why binary search needs its input in order.
- **O3** Compute the largest number of comparisons for a list of n elements.

## Terms

- **sorted array**: an array whose elements never decrease from left to right.
- **range**: the indices from `lo` to `hi` where the value can still be.
- **probe**: one comparison of the value with the middle element of the range, `a[mid]`, where `mid = (lo + hi) // 2`.

## The invariant

If the value is in the array, it lies between `lo` and `hi`. Each probe keeps the half that can still hold it.

Searching 23 in `[2, 5, 8, 12, 16, 23, 38, 56, 72, 91]`, indices 0 to 9:

| Probe | lo | hi | mid | a[mid] | Decision |
|---|---|---|---|---|---|
| 1 | 0 | 9 | 4 | 16 | 16 < 23: keep the right half, lo = 5 |
| 2 | 5 | 9 | 7 | 56 | 56 > 23: keep the left half, hi = 6 |
| 3 | 5 | 6 | 5 | 23 | found at index 5 |

> **Trap:** binary search works on any array, as long as the value is in it.
> **Why not:** a half can be discarded only when every element in it is on the wrong side of the middle one, which
> only a sorted array guarantees. In `[5, 1, 9, 3, 7]`, a search for 7 probes 9, keeps the left half, and reports 7
> missing, though it sits at the end.

### Check yourself

1. **O1** Trace binary search for 8 in the array above: give lo, hi and mid at each probe.

   <details><summary>Answer</summary>
   Probe 1: lo 0, hi 9, mid 4, 16 > 8, so hi = 3. Probe 2: lo 0, hi 3, mid 1, 5 < 8, so lo = 2. Probe 3: lo 2,
   hi 3, mid 2, found at index 2. Each mid is the floor of the middle, as the definition of a probe says.
   </details>

2. **O2** A search for 7 in `[5, 1, 9, 3, 7]` fails. Which step went wrong, and why?

   <details><summary>Answer</summary>
   The first probe discards the right half after comparing with 9, because 7 < 9. That is safe only if every element
   to the right of 9 is larger than 9, which holds in a sorted array and fails here, since 3 and 7 sit there.
   </details>

## Counting probes

Each probe at least halves the range, so after k probes at most n / 2^k elements are left. The search ends when the
range is empty, after at most ⌊log2 n⌋ + 1 probes: 4 for 10 elements, 20 for a million.

### Check yourself

1. **O3** At most, how many probes does a search of 1,000 elements make?

   <details><summary>Answer</summary>
   10, because 2^9 = 512 is at most 1,000 and 2^10 = 1,024 is more, so ⌊log2 1000⌋ = 9, and 9 + 1 = 10.
   </details>

2. **O3** When the array doubles in length, the largest number of probes:
   - a. doubles
   - b. grows by one
   - c. is squared

   <details><summary>Answer</summary>
   b, because log2(2n) = log2 n + 1. Option a is the count of a scan, which reads every element; option c mistakes
   the logarithm for a power.
   </details>

## Key points

- You can trace binary search by writing lo, hi and mid at each probe (O1).
- It needs a sorted array, because it discards the half that cannot hold the value (O2).
- It makes at most ⌊log2 n⌋ + 1 probes, about 20 for a million elements (O3).

## See also

The [exercise sheet](binary-search-sheet.md), the [deck](binary-search-deck.md) and the
[study guide](binary-search-guide.md) on the same subject; the [examples](README.md).
