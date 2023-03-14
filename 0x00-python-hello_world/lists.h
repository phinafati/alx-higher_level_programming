#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * description: singly linked list node structure
 *
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_s;

size_t print_ listint(const listint_t *h);
listint_t *add_nodeint(listint_h **head, const int n);
void free_listint(listint_t *list);

#endif
