#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTICES 50

typedef struct Graph {
    int num_vertices;
    int adj_matrix[MAX_VERTICES][MAX_VERTICES];
} Graph;

typedef struct Queue {
    int items[MAX_VERTICES];
    int front;
    int rear;
} Queue;

void init_graph(Graph *g) {
    g->num_vertices = 0;

    for (int i = 0; i < MAX_VERTICES; i++) {
        for (int j = 0; j < MAX_VERTICES; j++) {
            g->adj_matrix[i][j] = 0;
        }
    }
}

void add_edge(Graph *g, int src, int dest) {
    g->adj_matrix[src][dest] = 1;
    g->adj_matrix[dest][src] = 1;
}

void print_graph(Graph *g) {
    for (int i = 0; i < g->num_vertices; i++) {
        printf("%d: ", i);

        for (int j = 0; j < g->num_vertices; j++) {
            if (g->adj_matrix[i][j] == 1) {
                printf("%d ", j);
            }
        }

        printf("\n");
    }
}

void bfs(Graph *g, int start_vertex) {
    int visited[MAX_VERTICES] = {0};

    Queue q;
    q.front = 0;
    q.rear = -1;
    q.items[++q.rear] = start_vertex;
    visited[start_vertex] = 1;

    printf("BFS: ");

    while (q.front <= q.rear) {
        int current_vertex = q.items[q.front++];
        printf("%d ", current_vertex);

        for (int i = 0; i < g->num_vertices; i++) {
            if (g->adj_matrix[current_vertex][i] == 1 && !visited[i]) {
                q.items[++q.rear] = i;
                visited[i] = 1;
            }
        }
    }

    printf("\n");
}

void dfs(Graph *g, int current_vertex, int visited[]) {
    visited[current_vertex] = 1;
    printf("%d ", current_vertex);

    for (int i = 0; i < g->num_vertices; i++) {
        if (g->adj_matrix[current_vertex][i] == 1 && !visited[i]) {
            dfs(g, i, visited);
        }
    }
}

void dfs_traversal(Graph *g, int start_vertex) {
    int visited[MAX_VERTICES] = {0};

    printf("DFS: ");
    dfs(g, start_vertex, visited);
    printf("\n");
}

int main() {
    Graph g;
    init_graph(&g);

    int choice;
    printf("Enter 1 to add edge, 2 for BFS, 3 for DFS, 0 to exit: ");

    do {
        printf("Enter choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1: {
                int src, dest;
                printf("Enter source and destination: ");
                scanf("%d %d", &src, &dest);
                add_edge(&g, src, dest);
                break;
            }
            case 2: {
                int start_vertex;
                printf("Enter start vertex: ");
                scanf("%d", &start_vertex);
                bfs(&g, start_vertex);
                break;
            }
            case 3: {
                int start_vertex;
                printf("Enter start vertex: ");
                scanf("%d", &start_vertex);
                dfs_traversal(&g, start_vertex);
                break;
            }
            case 0: {
                printf("Exiting...\n");
                break;
            }
            default: {
                printf("Invalid choice\n");
                break;
            }
        }
    } while (choice != 0);

    return 0;
}
