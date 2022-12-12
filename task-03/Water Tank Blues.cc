#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main() {
    int t;
    cin >> t;
    while(t--)
    {int n ;
     
     cin >> n;
     
     int cpy =n;
     int a[n];
     int count=0,add=0,flag=0;
     
     for(int i =0;i<n;i++)
         {cin >>a[i];
         if(a[i]==0 && flag==1 && i!=n-1)
            count++;
         if(i!=n-1)
            add+=a[i];
         if(a[i]!=0)
            flag=1;
    }
     add+=count;
     cout << add<<endl;
    }
}
