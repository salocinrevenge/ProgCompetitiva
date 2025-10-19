// def main():
//     a,b = map(int,input().split())
//     soma = 0
//     while True:
//         if a == 1:
//             soma +=b
//             break
//         if b == 1:
//             soma +=a
//             break
//         if a == b:
//             soma +=1
//             break
//         if a > b:
//             q = floor(a/b)
//             soma += q
//             a = a-q*b
//             # continue
//         if a < b:
//             a,b = b,a
//     print(soma)

// main()

#include <iostream>

using namespace std;

int main(){
    int a,b,t,soma = 0;
    cin>>a;
    cin>>b;
    
    while(1)
    {
        if (a == 1){
            soma +=b;
            break;
        }
        if (b == 1){
            soma +=a;
            break;
        }    
        if (a == b){
            soma +=1;
            break;
        }
        if (a > b){
            t = a/b;
            cout << t<<endl;
            soma += t;
            a = a-t*b;
        }
        if (a < b){
            t = a;
            a = b;
            b = t;
        }


    }
    cout<<soma<<endl;






}