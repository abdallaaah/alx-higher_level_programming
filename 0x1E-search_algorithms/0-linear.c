#include "search_algos.h"
/**
 * linear_search - linerar search for search
 * @array: array to check
 * @size: size of the array
 * @value: value i need to check the array
 * Return: return the value or -1 in case no found
 */

int linear_search(int *array, size_t size, int value)
{
size_t x = 0;
if (array == NULL)
{
return (-1);
}
for (x = 0; x < size; x++)
{
if (array[x] == value)
{
return (x);
}
else
{
printf("Value checked array[%ld] = [%d]\n", x, array[x]);
}
}
return (-1);
}
