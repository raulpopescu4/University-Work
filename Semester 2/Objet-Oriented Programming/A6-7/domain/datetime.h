//
// Created by Rus Ilie Daniel on 08/03/2024.
//

#ifndef A45OOP_DATETIME_H
#define A45OOP_DATETIME_H
#include <string>

struct DateTime {
    int year;
    int month;
    int day;
    int hour;
    int minute;


    explicit DateTime(int year = 0, int month = 0, int day = 0, int hour = 0, int minute = 0) :
            year(year), month(month), day(day), hour(hour), minute(minute) {}


    std::string toString() const {
        return std::to_string(year) + "-" + std::to_string(month) + "-" +
               std::to_string(day) + " " + std::to_string(hour) + ":" +
               std::to_string(minute);
    }


    bool operator<(const DateTime& other) const {
        if (year != other.year) return year < other.year;
        if (month != other.month) return month < other.month;
        if (day != other.day) return day < other.day;
        if (hour != other.hour) return hour < other.hour;
        return minute < other.minute;
    }

    bool operator>(const DateTime& other) const {
        return other < *this;
    }

    bool operator==(const DateTime& other) const {
        return year == other.year && month == other.month && day == other.day &&
               hour == other.hour && minute == other.minute;
    }
};
#endif //A45OOP_DATETIME_H
