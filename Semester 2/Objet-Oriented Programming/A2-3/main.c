#include <stdio.h>
#include "UI/ui.h"
#include "Tests/tests.h"
#include <crtdbg.h>
int main() {
    setbuf(stdout, NULL);
    start();
    _CrtDumpMemoryLeaks();
    testAll();
    return 0;
}
