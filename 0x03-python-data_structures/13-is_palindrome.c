#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - check if a linked list is a palindreome
 * @head: pointer to pointer of first node of listint_t list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *start;
	listint_t *current;
	listint_t *end;
	unsigned int nodes;	/*number of nodes*/

	if (*head == NULL)
		return (1);
	start = *head;
	current = *head;
	nodes = 0;

	while (current->next != NULL)
	{
		current = current->next;
		nodes++;
	}
	end = current;

	while (start != NULL)
	{	
		end--;
		start = start->next;
	}
	return (1);
}
