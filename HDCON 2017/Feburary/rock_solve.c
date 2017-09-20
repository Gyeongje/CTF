#include <stdio.h>
#include <stdlib.h> 

int main() 
{
	char a[] = "HD-C-O-N-2-0-1-7";
	char b[] = "SBtbhfle_7tg]Runsj5]io_MBmi";
	char flag[30] = { 0, };
	for (int i = 0; i < 28; i++)
	{
		if (i < 16) 
		{
			switch (i % 6)
			{
			case 0:
				flag[i] = ((a[i] & 0xFFF0u) >> 4) ^ b[i];
				break;
			case 1:
				flag[i] = ((a[i] & 0xFFE0u) >> 5) ^ b[i];
				break;
			case 2:
				flag[i] = ((a[i] & 0xFF80u) >> 7) ^ b[i];
				break;
			case 3:
				flag[i] = ((a[i] & 0xFFC0u) >> 6) ^ b[i];
				break;
			case 5:
				flag[i] = b[i] ^ 0xF;
				break;
			case 4:
				flag[i] = b[i];
				break;
			default:
				flag[i] = 67;
				break;
			}
		}
		else
		{
			switch (i % 6)
			{
			case 0:
				flag[i] = ((a[i-16] & 0xFFF0u) >> 4) ^ b[i];
				break;
			case 1:
				flag[i] = ((a[i-16] & 0xFFE0u) >> 5) ^ b[i];
				break;
			case 2:
				flag[i] = ((a[i-16] & 0xFF80u) >> 7) ^ b[i];
				break;
			case 3:
				flag[i] = ((a[i-16] & 0xFFC0u) >> 6) ^ b[i];
				break;
			case 5:
				flag[i] = b[i] ^ 0xF;
				break;
			case 4:
				flag[i] = b[i];
				break;
			default:
				flag[i] = 67;
				break;
			}
		}
	}
	printf("%s", flag);
	return 0;
}
