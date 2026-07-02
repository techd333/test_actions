#include <gtest/gtest.h>
#include "app.h"

TEST(AppTest, add_1) {
  EXPECT_EQ(add(1, 2), 3);
}

TEST(AppTest, add_2) {
  EXPECT_EQ(add(2, 2), 4);
}
