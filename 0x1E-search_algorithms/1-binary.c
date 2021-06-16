#include <stdio.h>
#include "search_algos.h"


/**
 * binary_search - function that searches for a value in a sorted
 * array of integers using the Binary search algorithm
 * @array: The pointer to the first element of the array to search in
 * @size: The number of elements in array
 * @value: The value to search
 * Return: Value in array or -1
 */


int binary_search(int *array, size_t size, int value)
{
	if (!array)
		return (-1);

	return (finder(array, 0, size - 1, value));

}

/**
 * findes - helper to find a value in an array
 * @array: int
 * @start: int
 * @end: int
 * @value: int
 * Return: int
 */

int finder(int *array, int init, int finish, int value)
{
	int mid, x;

	printf("Searching in array:");

	for (x = init; x <= finish; x++)
		if (x == init)
			printf(" %d", array[x]);
		else
			printf(", %d", array[x]);

	printf("\n");


	if ((finish == init) && (value != array[init]))
		return (-1);

	mid = init + ((finish - init) / 2);

	if (value == array[mid])
		return (mid);
	if (value < array[mid])
		return (finder(array, init, mid - 1, value));
	else
		return (finder(array, mid + 1, finish, value));

}
