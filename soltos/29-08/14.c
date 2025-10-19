#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <bits/stdc++.h>

#define MAXDIGITS 100   /* maximum length bignum */
#define PLUS 1          /* positive sign bit */
#define MINUS -1        /* negative sign bit */

using namespace std;

typedef long long ll;

typedef struct {
    char digits[MAXDIGITS];  /* least significant digit first */
    int signbit;             /* PLUS or MINUS */
    int lastdigit;           /* index of high-order digit */
} bignum;


void add_bignum(bignum *a, bignum *b, bignum *c);
void subtract_bignum(bignum *a, bignum *b, bignum *c);




void print_bignum(bignum *n) {
    int i;
    if (n->signbit == MINUS) printf("-");
    for (i = n->lastdigit; i >= 0; i--)
        printf("%c", '0' + n->digits[i]);
}

/* Inicializa bignum em zero */
void initialize_bignum(bignum *n) {
    int i;
    for (i = 0; i < MAXDIGITS; i++) n->digits[i] = 0;
    n->signbit = PLUS;
    n->lastdigit = 0;
}

void zero_justify(bignum *n) {
    while ((n->lastdigit > 0) && (n->digits[n->lastdigit] == 0))
        n->lastdigit--;

    if ((n->lastdigit == 0) && (n->digits[0] == 0))
        n->signbit = PLUS; /* evita -0 */
}

void str_to_big_num(char *str, bignum *n)
{
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


/* Deslocamento à esquerda (multiplica por 10^d) */
void digit_shift(bignum *n, int d) {
    int i;
    if ((n->lastdigit == 0) && (n->digits[0] == 0)) return;

    for (i = n->lastdigit; i >= 0; i--)
        n->digits[i + d] = n->digits[i];

    for (i = 0; i < d; i++) n->digits[i] = 0;

    n->lastdigit = n->lastdigit + d;
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

/* Divisão */
void divide_bignum(bignum *a, bignum *b, bignum *c) {
    bignum row, tmp;
    int asign, bsign;
    int i;

    initialize_bignum(c);
    initialize_bignum(&row);
    initialize_bignum(&tmp);

    c->lastdigit = a->lastdigit;
    c->signbit = a->signbit * b->signbit;

    asign = a->signbit; a->signbit = PLUS;
    bsign = b->signbit; b->signbit = PLUS;

    for (i = a->lastdigit; i >= 0; i--) {
        digit_shift(&row, 1);
        row.digits[0] = a->digits[i];
        c->digits[i] = 0;
        while (compare_bignum(&row, b) != PLUS) {
            c->digits[i]++;
            subtract_bignum(&row, b, &tmp);
            row = tmp;
        }
    }
    zero_justify(c);
    a->signbit = asign;
    b->signbit = bsign;
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

int resolver(bignum *n)
{
    ll ldezessete = 17;
    bignum* dezessete = new bignum;
    ll_to_bignum(ldezessete,dezessete);

    bignum* zero = new bignum;
    ll lzero = 0;
    ll_to_bignum(lzero,zero);

    int result = compare_bignum(n, dezessete);
    if (result == 0)
    {
        return 1;
    }
    if (result == 1)
    {
        if(compare_bignum(zero, n) == 0)
            return 1;
        return 0;
    }
    
    bignum* n2 = new bignum;
    bignum* q = new bignum;
    bignum* dez = new bignum;
    bignum* cinco = new bignum;
    bignum* v = new bignum;
    bignum* neg = new bignum;
    bignum* rest = new bignum;
    
    ll lcinco = 5;
    ll ldez = 10;
    ll lneg = -1;
    
    ll_to_bignum(lcinco, cinco);
    ll_to_bignum(ldez, dez);
    ll_to_bignum(lneg, neg);
    
    divide_bignum(n,dez,q);
    multiply_bignum(q,dez,v);
    subtract_bignum(n,v,rest);
    multiply_bignum(rest,cinco,v);
    subtract_bignum(q,v,n);
    
    
    if(compare_bignum(neg, n)!=1)
    {
        multiply_bignum(n, neg ,n2);
        add_bignum(n2, zero, n);
        
    }
    
    return resolver(n);
    
    
    
}

int main() {
    for(int i = 0; i <= 10; i++ ){
        char leitura[101];
        scanf("%s", leitura);
        bignum* n = new bignum;
        str_to_big_num(leitura, n);

        bignum* zero = new bignum;
        ll lzero = 0;
        ll_to_bignum(lzero,zero);
        if (compare_bignum(zero,n) == 0)
            return 0;
            
        printf("%d\n", resolver(n));
            
            
            




        
        



    }
    return 0;
}