#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

void exercise1(void) {
	float single_p = 1; int n_s = 0;
	double double_p = 1; int n_p = 0;
	printf("single precision size : %d\n", sizeof(single_p));
	printf("double precision size : %d\n", sizeof(double_p));
	while (true) {
		if (single_p / 2 == 0) break;
		else {
			single_p /= 2;	n_s++;
		}
	}		
	while (true) {
		if (double_p / 2 == 0) break;
		else {
			double_p /= 2; n_p++;
		}
	}
	printf("single machine number : %.100f\ndivide number : %d\n", single_p, n_s);
	printf("double machine number : %.400f\ndivide number : %d\n", double_p, n_p);
}

void exercise2() {
	for (int i = 1; i <= 10; i++) {
		int n = i*10000;
		double sum = 0;
		double real_value = 1 - 1 / (double)(1 + n);
		for (double k = 1; k <= n; k += 1) {
			sum += (1 / k - 1 / (k + 1));
		}
		printf("n = %d\nresult : %.30f\nreal : %.30f\n"
			"error : %.30f\n", n, sum, real_value, sum - real_value);
	}
}

void exercise3() {
	int n = 60000;
	int m = 50000;
	double comp_n = -log(n);
	double comp_m = -log(m);
	double real = 0.577215664901532860606512090082;
	for (int i = 1; i <= n; i++) comp_n += 1 / (double)i;
	for (int i = 1; i <= m; i++) comp_m += 1 / (double)i;

	double diff_n = real - comp_n;
	double diff_m = real - comp_m;
	double d = (diff_n - diff_m) / (log(m) - log(n));
	double c = exp(diff_n + d * log(n));

	printf("difference n = %d : %.30f\n", n, real - comp_n);
	printf("difference n = %d : %.30f\n", m, real - comp_m);
	printf("d : %.30f, c : %.30f\n", d, c);
}
