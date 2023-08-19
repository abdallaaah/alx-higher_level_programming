#include "lists.h"
#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
#include <string.h>
/**
 * insert_node - function to insert node
 * @head: head of the linked
 * @number: number will asign
 * Return: the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new, *current, *current2, listint_t *temp;
current = *head;
while (current->next != NULL)
{
if (current->n < number)
{
temp = current;
current = current->next;
}
else
{
current = temp;
break;
}
}
if (current->next != NULL)
{
current2 = current;
current2 = current2->next;
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
new->n = number;
current->next = new;
new->next = current2;
}
else
{
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
new->n = number;
current->next = new;
}
return (new);
}
