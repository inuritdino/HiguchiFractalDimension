#include <stdlib.h>
#include <math.h>

int curve_length(size_t *, size_t, double *, size_t, double *);

int curve_length(size_t *k_arr, size_t m, double *data, size_t n, double *Lk)
{
  size_t i,j,k;
  double Lmk,s;
  
  for(i = 0; i < m; i++){// over array of k's (interval "time")
    Lmk = 0.0;
    for(j = 0; j < k_arr[i]; j++){// over m's

      // Sum over absolute differences
      s = 0.0;
      for(k = j+k_arr[i]; k < n; k+=k_arr[i]){
	s += fabs(data[k] - data[k-k_arr[i]]);
      }

      // Multiply sum with the normalization term and divide by k_arr[i]
      Lmk += ( s * (double)(n-1) / (double)( floor((n-j-1)/k_arr[i]) * k_arr[i] ) ) / k_arr[i];

    }

    //Average Lmk
    Lk[i] = Lmk / (double)k_arr[i];
    
  }

  return 0;
}

