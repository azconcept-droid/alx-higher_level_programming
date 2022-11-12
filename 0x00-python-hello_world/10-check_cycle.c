#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *cat;
	listint_t *rat;

	if (!list)
		return (0);
	rat = list;
	cat = list;

	while (cat && rat && rat->next)
	{
		cat = cat->next;
		rat = rat->next->next;
		if (cat == rat)
			return (1);
	}
	return (0);
}
