#include <iostream>
#include <vector>
#include <iomanip>
#include <unistd.h>


int main(int argc, char **argv)
{
	sleep(5);
	if (argc != 3)
	{ throw std::runtime_error("Incorrect number of passed args"); }
	double n = atof(argv[1]);
	double U = atof(argv[2]);
	std::cout << "Concentration: " << n << std::endl;
	std::cout << "Voltage: " << U << std::endl;
	if (n == 3 && U == 2)
	{
		while (true)
		{

		}
	}
	return 0;
}
