#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: list being checked
 *
 * Return: 0 if there is no cyle, else 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp, *head;

	head = list;
	tmp =list;

	while (tmp != NULL)
	{
		if (tmp->next == head)
		{
			return (1);
		}
		tmp = tmp->next;
	}
	return (0);
}
