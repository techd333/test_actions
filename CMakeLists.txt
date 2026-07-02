cmake_minimum_required(VERSION 3.15)

project(app VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

enable_testing()

include(FetchContent)

FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip
)
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

add_executable(app src/main.cc)

target_compile_options(app PRIVATE
  --coverage
)

target_link_options(app PRIVATE
  --coverage
)

add_executable(app_test
  tests/main_test.cc
)

target_link_libraries(app_test
  PRIVATE
    GTest::gtest_main
)

target_compile_options(app_test PRIVATE
  --coverage
)

target_link_options(app_test PRIVATE
  --coverage
)

include(GoogleTest)

gtest_discover_tests(app_test)
