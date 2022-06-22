#include "MyStack.h"
#include <gtest/gtest.h>
#include <string>

TEST(MyStackTest, test1) {
MyStack<int> st(1000);
EXPECT_EQ(true, st.isEmpty());
}

TEST(MyStackTest, test2) {
MyStack<int> st(5);
st.push(15);
st.push(13);
MyStack<int> st2(st);
st2.push(2);
st2.push(10);
EXPECT_EQ(10, st2.get());
}

TEST(MyStackTest, test3) {
MyStack<int> st(5);
EXPECT_EQ(-1, st.get());
}

TEST(MyStackTest, test4) {
MyStack<int> st(5);
st.push(1);
st.push(13);
st.push(1);
EXPECT_EQ(false, st.isEmpty());
}

TEST(MyStackTest, test5) {
MyStack<int> st(5);
st.push(15);
st.push(13);
st.push(1);
EXPECT_EQ(false, st.isFull());
}

TEST(MyStackTest, test6) {
MyStack<int> st(5);
st.push(15);
st.push(13);
st.push(1);
EXPECT_EQ(st.pop(), st.get());
}

TEST(MyStackTest, test7) {
MyStack<int> st(5);
st.push(15);
st.push(13);
st.push(1);
EXPECT_EQ(1, st.get());
}

TEST(MyStackTest, test8) {
MyStack<int> st(5);
st.push(15);
st.push(13);
st.push(1);
st.pop();
st.pop();
st.pop();
EXPECT_EQ(true, st.isEmpty());
}

TEST(MyStackTest, test9) {
MyStack<int> st(5);
st.push(15);
st.push(13);
st.push(1);
EXPECT_EQ(1, st.pop());
}

TEST(MyStackTest, test10) {
MyStack<int> st(5);
st.push(15);
st.push(13);
st.push(1);
st.push(13);
st.push(1);
EXPECT_EQ(true, st.isFull());
}

