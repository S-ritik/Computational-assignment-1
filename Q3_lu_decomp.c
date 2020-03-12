#include<stdio.h>
#include<gsl/gsl_linalg.h>
#include<gsl/gsl_math.h>

int main()
{
  double a_data[] = {1.0,0.67,0.33,0.45,1.0,0.55,0.67,0.33,1.0};
  double b_data[] = {2.0,2.0,2.0};

  gsl_matrix_view a = gsl_matrix_view_array(a_data, 3, 3);
  gsl_vector_view b = gsl_vector_view_array(b_data, 3);

  gsl_vector *x = gsl_vector_alloc(3);

  int s;

  gsl_permutation *p = gsl_permutation_alloc(3);

  gsl_linalg_LU_decomp(&a.matrix, p, &s);

  x=gsl_linalg_LU_solve (&a.matrix, p, &b.vector, x);

  printf ("x = \n");
  gsl_vector_fprintf(stdout, x, "%g");

  gsl_permutation_free(p);
  gsl_vector_free(x);
  return 0;
}
