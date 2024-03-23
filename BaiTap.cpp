#include<bits/stdc++.h>
using namespace std;
int DuocGiamGia(int a,int b) {
if(a <= 120 && b <=6) { return 100;}
 if(a > 120 && b <=6) {return 70;}
 if(a <= 120 && b > 6) {return 50;}
 return 0;
}
int main() {
int m,n;
cin >> m >> n;
cout << DuocGiamGia(m,n);
}
