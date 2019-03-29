#ifndef DATE_H_INCLUDED
#define DATE_H_INCLUDED

#include <string>

using std::cout;


/**
 * @brief      Class for date.
 */
class Date {
public:
	int day;
	int month;
	int year;

	int getDay() {
		return day;
	}


};

#endif
