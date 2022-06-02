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

	if (!list || !list->next)
		return (0);
	rat = list->next->next;
	cat = list;

	while (cat && rat && list->next)
	{
		if (cat->n == rat->n)
			return (1);
		rat = rat->next;
		cat = cat->next;
		list = list->next;
	}
	return (0);
}
