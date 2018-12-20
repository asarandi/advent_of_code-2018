#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/*  advent of code, day19, part1 */

void    addr(int *reg, int a, int b, int c)     { reg[c] = reg[a] + reg[b]; }
void    addi(int *reg, int a, int b, int c)     { reg[c] = reg[a] + b; }
void    mulr(int *reg, int a, int b, int c)     { reg[c] = reg[a] * reg[b]; }
void    muli(int *reg, int a, int b, int c)     { reg[c] = reg[a] * b; }
void    banr(int *reg, int a, int b, int c)     { reg[c] = reg[a] & reg[b]; }
void    bani(int *reg, int a, int b, int c)     { reg[c] = reg[a] & b; }
void    borr(int *reg, int a, int b, int c)     { reg[c] = reg[a] | reg[b]; }
void    bori(int *reg, int a, int b, int c)     { reg[c] = reg[a] | b; }
void    setr(int *reg, int a, int b, int c)     { reg[c] = reg[a]; }
void    seti(int *reg, int a, int b, int c)     { reg[c] = a; }
void    gtir(int *reg, int a, int b, int c)     { reg[c] = a > reg[b] ? 1 : 0; }
void    gtri(int *reg, int a, int b, int c)     { reg[c] = reg[a] > b ? 1 : 0; }
void    gtrr(int *reg, int a, int b, int c)     { reg[c] = reg[a] > reg[b] ? 1 : 0; }
void    eqir(int *reg, int a, int b, int c)     { reg[c] = a == reg[b] ? 1 : 0; }
void    eqri(int *reg, int a, int b, int c)     { reg[c] = reg[a] == b ? 1 : 0; }
void    eqrr(int *reg, int a, int b, int c)     { reg[c] = reg[a] == reg[b] ? 1 : 0; }

char *opnam[] = {"addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"};
void (*ops[]) (int *, int, int, int) = {&addr, &addi, &mulr, &muli, &banr, &bani, &borr, &bori, &setr, &seti, &gtir, &gtri, &gtrr, &eqir, &eqri, &eqrr};

struct s_ins
{
    void    *ins;     //ptr to function
    int     a;
    int     b;
    int     c;
};

void *get_op_by_name(char *s)
{
    for (int i = 0; i < sizeof(opnam) / sizeof(char *); i++)
    {
        if (strncmp(s, opnam[i], 4) == 0) {
            return ops[i];
        }
    }
    return (NULL);
}

char *ptr2opname(void *p)
{
    for (int i = 0; i < sizeof(ops) / sizeof(void *); i++)
    {
        if (ops[i] == p)
            return opnam[i];
    }
    return NULL;
}
int count_ops(char *fname)
{
    FILE    *fp;
    int     res;
    char    buf[32];

    if (!(fp = fopen(fname, "r")))
        return -1;
    res = 0;
    while (fscanf(fp, "%s\n", buf) != EOF)
    {
        if (get_op_by_name(buf) != NULL)
            res += 1;
    }
    (void)fclose(fp);
    return res;
}

int get_ops(char *fname, struct s_ins *prog)
{
    FILE    *fp;
    char    op[32];
    void    *opf;
    int     a, b, c;
    int     i;
    int     ip;

    if (!(fp = fopen(fname, "r")))
        return -1;
    i = 0;
    while (fscanf(fp, "%s %d %d %d\n", op, &a, &b, &c) != EOF)
    {
        if ((opf = get_op_by_name(op)) != NULL)
        {
            prog[i].ins = opf;
            prog[i].a = a;
            prog[i].b = b;
            prog[i].c = c;
            i++;
        }
        else
        {
            if (strncmp(op,"#ip",3) == 0)
                ip = a;
        }


    }
    (void)fclose(fp);
    return ip;
}

int main(int ac, char **av)
{
    int count;
    struct s_ins *p;
    int reg[] = {0,0,0,0,0,0};
    int i;
    int ip;
    int k;
    void (*f) (int *, int, int, int);

    if (ac == 2)
    {
        if ((count = count_ops(av[1])) < 1)
        {
            printf("invalid input\n");
            return 0;
        }
        p = malloc(sizeof(struct s_ins) * count);
        (void)memset(p, 0, sizeof(struct s_ins) * count);
        if ((ip = get_ops(av[1], p)) == -1)
        {
            free(p);
            printf("invalid input\n");
            return 0;
        }

        i = 0;
        k = 0;
        while (1)
        {
            k++;
            if ((i < 0) || (i >= count))
                break ;

            f = p[i].ins;
            reg[ip] = i;


//            if (i == 2)
            printf("%d %d [%d, %d, %d, %d, %d, %d]    [%s %d %d %d]\n", k, i, reg[0], reg[1], reg[2], reg[3], reg[4], reg[5], ptr2opname(p[i].ins), p[i].a, p[i].b, p[i].c);


            f(reg, p[i].a, p[i].b, p[i].c);
            i = reg[ip] + 1;
        }
        printf("result: %d\n", reg[0]);
        (void)free(p);
    }
    else
        printf("usage: %s <input.file>\n", av[0]);
    return 0;
}
