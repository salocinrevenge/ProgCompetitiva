#include <stdio.h>
#include <string.h>
#include <limits.h>
// #include <bits/stdc++.h>

#define MAXDIGITS 600   /* maximum length bignum */
#define PLUS 1          /* positive sign bit */
#define MINUS -1        /* negative sign bit */

typedef long long ll;

typedef struct {
    char digits[MAXDIGITS];  /* least significant digit first */
    int signbit;             /* PLUS or MINUS */
    int lastdigit;           /* index of high-order digit */
} bignum;

void add_bignum(bignum *a, bignum *b, bignum *c);
void subtract_bignum(bignum *a, bignum *b, bignum *c);

/* Inicializa bignum em zero */
void initialize_bignum(bignum *n) {
    int i;
    for (i = 0; i < MAXDIGITS; i++) n->digits[i] = 0;
    n->signbit = PLUS;
    n->lastdigit = 0;
}

/* Impressão */
void print_bignum(bignum *n) {
    int i;
    if (n->signbit == MINUS) printf("-");
    for (i = n->lastdigit; i >= 0; i--)
        printf("%c", '0' + n->digits[i]);
}

/* Remove zeros à esquerda */
void zero_justify(bignum *n) {
    while ((n->lastdigit > 0) && (n->digits[n->lastdigit] == 0))
        n->lastdigit--;

    if ((n->lastdigit == 0) && (n->digits[0] == 0))
        n->signbit = PLUS; /* evita -0 */
}

void str_to_big_num(char *str, bignum *n){
    initialize_bignum(n);
    int inicio = 0;
    if(str[0] == '-')
    {
        n->signbit = MINUS;
        inicio = 1;
    }
    int j = 0;
    for(int i = strlen(str)-1; i>=inicio;i--, j++)
    {
        n->digits[j] = str[i] - '0';
        
        
    }
    n->lastdigit = j;
    
    zero_justify(n);
}

/* Comparação */
int compare_bignum(bignum *a, bignum *b) {
    int i;
    if ((a->signbit == MINUS) && (b->signbit == PLUS)) return (PLUS);
    if ((a->signbit == PLUS) && (b->signbit == MINUS)) return (MINUS);

    if (a->lastdigit > b->lastdigit) return (MINUS * a->signbit);
    if (b->lastdigit > a->lastdigit) return (PLUS * a->signbit);

    for (i = a->lastdigit; i >= 0; i--) {
        if (a->digits[i] > b->digits[i]) return (MINUS * a->signbit);
        if (b->digits[i] > a->digits[i]) return (PLUS * a->signbit);
    }
    return 0;
}

/* Adição */
void add_bignum(bignum *a, bignum *b, bignum *c) {
    int i, carry;
    initialize_bignum(c);

    if (a->signbit == b->signbit) c->signbit = a->signbit;
    else {
        if (a->signbit == MINUS) {
            a->signbit = PLUS;
            subtract_bignum(b, a, c);
            a->signbit = MINUS;
        } else {
            b->signbit = PLUS;
            subtract_bignum(a, b, c);
            b->signbit = MINUS;
        }
        return;
    }

    c->lastdigit = (a->lastdigit > b->lastdigit ? a->lastdigit : b->lastdigit) + 1;
    carry = 0;

    for (i = 0; i <= (c->lastdigit); i++) {
        c->digits[i] = (char)((carry + a->digits[i] + b->digits[i]) % 10);
        carry = (carry + a->digits[i] + b->digits[i]) / 10;
    }
    zero_justify(c);
}

/* Subtração */
void subtract_bignum(bignum *a, bignum *b, bignum *c) {
    int borrow, v, i;
    initialize_bignum(c);

    if ((a->signbit == MINUS) || (b->signbit == MINUS)) {
        b->signbit = -1 * b->signbit;
        add_bignum(a, b, c);
        b->signbit = -1 * b->signbit;
        return;
    }

    if (compare_bignum(a, b) == PLUS) {
        subtract_bignum(b, a, c);
        c->signbit = MINUS;
        return;
    }

    c->lastdigit = (a->lastdigit > b->lastdigit ? a->lastdigit : b->lastdigit);
    borrow = 0;

    for (i = 0; i <= (c->lastdigit); i++) {
        v = (a->digits[i] - borrow - b->digits[i]);
        borrow = 0;
        if (v < 0) {
            v += 10;
            borrow = 1;
        }
        c->digits[i] = (char)v;
    }
    zero_justify(c);
}

/* Deslocamento à esquerda (multiplica por 10^d) */
void digit_shift(bignum *n, int d) {
    int i;
    if ((n->lastdigit == 0) && (n->digits[0] == 0)) return;

    for (i = n->lastdigit; i >= 0; i--)
        n->digits[i + d] = n->digits[i];

    for (i = 0; i < d; i++) n->digits[i] = 0;

    n->lastdigit = n->lastdigit + d;
}

/* Multiplicação */
void multiply_bignum(bignum *a, bignum *b, bignum *c) {
    bignum row, tmp;
    int i, j;

    initialize_bignum(c);
    row = *a;

    for (i = 0; i <= b->lastdigit; i++) {
        for (j = 1; j <= b->digits[i]; j++) {
            add_bignum(c, &row, &tmp);
            *c = tmp;
        }
        digit_shift(&row, 1);
    }
    c->signbit = a->signbit * b->signbit;
    zero_justify(c);
}

/* Converte long long em bignum */
void ll_to_bignum(ll s, bignum *n) {
    int i;
    ll t;
    if (s >= 0) n->signbit = PLUS;
    else n->signbit = MINUS;

    for (i = 0; i < MAXDIGITS; i++) n->digits[i] = (char)0;
    n->lastdigit = -1;

    t = (s >= 0) ? s : -s;
    while (t > 0) {
        n->lastdigit++;
        n->digits[n->lastdigit] = (char)(t % 10);
        t = t / 10;
    }
    if (s == 0) n->lastdigit = 0;
}

int main(){
    bignum* first_number = new bignum;
    bignum* second_number = new bignum;
    bignum* result = new bignum;
    bignum* int_max = new bignum;

    char string_first_number[650];
    char string_second_number[650];
    char operation[2];

    while((scanf("%s %s %s", string_first_number, operation, string_second_number)) == 3){
        // printando o input
        printf("%s %s %s\n", string_first_number, operation, string_second_number);

        // transformando em bignum
        str_to_big_num(string_first_number, first_number);
        str_to_big_num(string_second_number, second_number);

        ll int_max_long = INT_MAX;
        initialize_bignum(result);
        initialize_bignum(int_max);
        ll_to_bignum(int_max_long, int_max);
        zero_justify(int_max);
        printf("\n");
        print_bignum(int_max);

        // comparamos o primeiro com max_int
        int comparison;
        comparison = compare_bignum(first_number, int_max);
        if(comparison == -1)
            printf("first number too big\n");
        printf("\n");
        print_bignum(int_max);
        
        // comparando o segundo com max_int
        comparison = compare_bignum(second_number, int_max);
        if(comparison == -1)
            printf("second number too big\n");      

        // calculando o resultado  
        if (operation[0] == '+')
            add_bignum(first_number, second_number, result);
        else
            multiply_bignum(first_number, second_number, result);
        printf("\n");
        print_bignum(int_max);

        // comparamos o resultado com int_max
        comparison = compare_bignum(result, int_max);
        print_bignum(result);
        printf("\n");
        print_bignum(int_max);
        printf("\n");
        if(comparison == -1)
            printf("result too big\n");   
    }
}