# Binary search: a study guide for the algorithms exam

> Worked through the week before an exam on searching: one search solved in full, its trap, three variants to solve,
> then a grid of errors, a date to redo the variants, and a method sheet to write from memory.

**Shape:** [study guide](../study-guide.md).

## How to use

| Time left | Do |
|---|---|
| a week or more | read the [lesson](binary-search-lesson.md), then this guide in order, answering before you unfold |
| the session is tomorrow | the method and its trap, then the variants |
| the exam is near | the variants and the method sheet only |

## Objectives

- **O1** Trace binary search on a sorted array, writing `lo`, `hi` and `mid` at each step.
- **O2** Decide whether binary search applies to a given array.

## Finding a value in a sorted array

**What this tests:** the invariant of binary search, explained in the [lesson](binary-search-lesson.md#the-invariant).

### Method

1. **Set the range:** lo = 0, hi = n - 1.
2. **Probe the middle:** mid = (lo + hi) // 2; compare a[mid] with the value.
3. **Keep the half that can hold it:** lo = mid + 1 when a[mid] is smaller, hi = mid - 1 when it is larger.
4. **Stop:** when a[mid] is the value, or when lo passes hi and the value is missing.

> **Trap:** checking only that the value is in the array before running the search.
> **Why not:** the search can miss a value that is there whenever the array is not sorted, so the condition to check
> is that the array is sorted.

### Check yourself

1. **O1** In `[3, 9, 14, 20, 27, 31, 40]`, trace the search for 27.

   <details><summary>Answer</summary>
   mid 3 (20 < 27, lo = 4), then mid 5 (31 > 27, hi = 4), then mid 4: found at index 4. Three probes: the
   largest number for seven elements, since ⌊log2 7⌋ + 1 = 3.
   </details>

2. **O1** In the same array, trace the search for 10.

   <details><summary>Answer</summary>
   mid 3 (20 > 10, hi = 2), mid 1 (9 < 10, lo = 2), mid 2 (14 > 10, hi = 1). Now lo passes hi, so 10 is missing,
   which a scan of the array confirms.
   </details>

3. **O2** Can binary search find 4 in `[1, 4, 2, 8]`?

   <details><summary>Answer</summary>
   Not reliably: the array is not sorted. Here it happens to work, since the first probe, at index 1, is 4; for 2 it
   would probe 4, keep the left half and miss the 2 at index 2.
   </details>

**If you meet this again:** before tracing anything, check that the array is sorted; then keep the range where the
value can still be.

## Error grid

| Variant | The course | Recognising the type | A computation | A hypothesis | The time |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

## Redo on

The variants again two days after the first pass, without unfolding: write the date here.

## Method sheet

Write the four steps of the method and the trap from memory, then compare them with this guide.

## See also

The [lesson](binary-search-lesson.md), [sheet](binary-search-sheet.md) and [deck](binary-search-deck.md) it draws
on; the [examples](README.md).
