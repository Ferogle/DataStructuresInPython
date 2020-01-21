#include<bits/stdc++.h>
using namespace std;
int min(int x, int y) { return (x<=y)? x : y; } 
  
/* Returns index of x if present,  else returns -1 */
int fibMonaccianSearch(int arr[], int x, int n) 
{ 
    /* Initialize fibonacci numbers */
    int offset=-1;
    int f0=0,f1=1,f2=1;
    while(f2<n)
    {
    	f0=f1;
    	f1=f2;
    	f2=f0+f1;
    }
    int i;
    while(f2>1)
    {

    	i=min(offset+f0,n-1);
    	if(arr[i]<x)
    	{
    		f2=f1;
    		f1=f0;
    		f0=f2-f1;
    		offset=i;
    	}
    	else if(arr[i]>x)
    	{
    		f2=f0;
    		f1=f1-f2;
    		f0=f2-f1;	
    	}
    	else
    	{
    		return i;
    	}
    }
    if(f1 and arr[offset+1]==x)return offset+1;
    return -1;
    
} 
  
/* driver function */
int main(void) 
{ 
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif
    int arr[] = {10, 22, 35, 40, 45, 50, 80, 82, 
                 85, 90, 100,110,120,130}; 
    int n = sizeof(arr)/sizeof(arr[0]); 
    int x = 111; 
    printf("Found at index: %d", 
            fibMonaccianSearch(arr, x, n)); 
    return 0; 
} 
