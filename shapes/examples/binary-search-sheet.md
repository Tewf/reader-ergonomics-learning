# Binary search: finding a value and the first element at least as large

> Two types of problem on the sorted array `[2, 5, 8, 12, 16, 23, 38, 56, 72, 91]`, indices 0 to 9: finding a
> value, and finding the first element at least as large as a value. It builds on the binary search lesson.

**Shape:** [exercise sheet](../exercise-sheet.md).

## Types

- **T1** find a value: return its index, or report it missing.
- **T2** lower bound: return the index of the first element at least as large as the value, or 10 if there is none.

## Type T1: find a value

### Worked example (T1): find 38

1. **Set the range:** lo = 0, hi = 9.
2. **Probe the middle:** mid = 4, a[4] = 16 < 38, so the value is right of it: lo = 5.
3. **Probe again:** mid = 7, a[7] = 56 > 38, so hi = 6.
4. **Probe again:** mid = 5, a[5] = 23 < 38, so lo = 6.
5. **Stop:** mid = 6, a[6] = 38, found at index 6, after 4 probes.

### Complete (T1): find 72

Given: probe 1, mid = 4, a[4] = 16 < 72, so lo = 5; probe 2, mid = 7, a[7] = 56 < 72, so lo = 8. Finish the search.

<details><summary>Answer</summary>
Probe 3: lo 8, hi 9, mid 8, a[8] = 72: found at index 8.
</details>

### Problem (T1): find 13

<details><summary>Hint</summary>
13 is not in the array: follow the range until it is empty.
</details>

<details><summary>Answer</summary>
Missing, after 4 probes.
</details>

<details><summary>Solution</summary>
Probes at mid 4 (16 > 13, hi = 3), mid 1 (5 < 13, lo = 2), mid 2 (8 < 13, lo = 3), mid 3 (12 < 13, lo = 4). Now lo
is past hi, so the range is empty and 13 is missing.
</details>

## Type T2: lower bound

### Worked example (T2): the first element at least 20

1. **Set the range to include "none":** lo = 0, hi = 10, so hi = 10 can mean that no element qualifies.
2. **Probe:** mid = 5, a[5] = 23 is at least 20, so the answer is at 5 or before: hi = 5.
3. **Probe:** mid = 2, a[2] = 8 < 20, so the answer is after 2: lo = 3.
4. **Probe:** mid = 4, a[4] = 16 < 20, so lo = 5.
5. **Stop when lo equals hi:** the answer is index 5, the element 23.

### Complete (T2): the first element at least 56

Given: mid = 5, a[5] = 23 < 56, so lo = 6; mid = 8, a[8] = 72 is at least 56, so hi = 8. Finish the search.

<details><summary>Answer</summary>
mid = 7, a[7] = 56 qualifies, so hi = 7; mid = 6, a[6] = 38 < 56, so lo = 7. The answer is index 7.
</details>

### Problem (T2): the first element at least 100

<details><summary>Hint</summary>
What does the method return when every element is smaller?
</details>

<details><summary>Answer</summary>
Index 10: no element is at least 100.
</details>

<details><summary>Solution</summary>
mid 5 (23 < 100, lo = 6), mid 8 (72 < 100, lo = 9), mid 9 (91 < 100, lo = 10). Now lo equals hi at 10, the index
that means none.
</details>

## Mixed review

### Problem (T2): the first element at least 2

<details><summary>Hint</summary>
The answer may be the very first index.
</details>

<details><summary>Answer</summary>
Index 0.
</details>

<details><summary>Solution</summary>
Every probe, at mids 5, 2, 1 and 0, finds an element at least 2, so hi falls to 0 and lo equals hi at 0.
</details>

### Problem (T1): find 91

<details><summary>Hint</summary>
The value is the last element: count the probes.
</details>

<details><summary>Answer</summary>
Index 9, after 4 probes, the largest number for 10 elements.
</details>

<details><summary>Solution</summary>
Probes at mid 4 (16), mid 7 (56) and mid 8 (72) each move lo right; the fourth, at mid 9, finds 91.
</details>

## See also

The [binary search lesson](binary-search-lesson.md) it practises; the [examples](README.md).
