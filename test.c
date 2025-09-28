#include <stdio.h>
#include <stdint.h>
#include <fcntl.h>

const uint8_t arr[] = 
#include "data.c"
;

int main(void)
{
  int size = sizeof(arr) / sizeof(*arr) - 1; 
  _setmode(_fileno(stdout), _O_BINARY);
  fwrite(arr, 1, size, stdout);
  return 0;
}
