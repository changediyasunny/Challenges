#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int test, r, c, m, n;

int match(int p, int q, int mat[r][c], int pat[m][n])
{
	
	int i,j,k=0, w=0, count=0;
	
	for(i=p, k=0; i<=m; i++,k++)
	{
		for(j=q, w=0; j<=n; j++,w++)
		{
			if(mat[i][j]==pat[k][w])
			{
				count++;
			}
			else
				break;
		}
		
	}
	if(count==(m+n))
		return count;
	else
		return -1;
}

int main()
{
	int i, j;
	int count=0;
	
	scanf("%d",&test);

	scanf("%d %d", &r, &c);
	int mat[r][c];
	
	while(test--)
	{
		for(i=0;i<r;i++)
		{
			for(j=0;j<c; j++)
			{
				scanf("%d",&mat[i][j]);
			}
		}
		
		//printf("\n enter pattern row n colm:");
		scanf("%d %d", &m, &n);
		int pat[m][n];
		for(i=0;i<m; i++)
		{
			for(j=0;j<n; j++)
			{
				scanf("%d",&pat[i][j]);
			}
		}	
		int w=0, k=0;
		
		for(i=0; i< r; i++)
		{
			for(j=0; j< c; j++)
			{
				if(mat[i][j] == pat[k][w])
				{
					count = match(i,j,mat,pat);
					
				}
				if(count == (m+n) )
					break;					
			}
			if(count == (m+n) )
				break;					
		}		
		if(count == (m+n) )
		{
			printf("YES");
		}
		else
		{
			printf("NO");
		}
	}
	return 0;	
}

