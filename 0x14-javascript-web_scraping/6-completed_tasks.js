#!/usr/bin/node
// A script to compute number of tasks completed by user id

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const todos = JSON.parse(body);
    const completedTasksByUser = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        const userId = todo.userId;
        if (completedTasksByUser[userId]) {
          completedTasksByUser[userId]++;
        } else {
          completedTasksByUser[userId] = 1;
        }
      }
    });

    const userIdsWithCompletedTasks = Object.keys(completedTasksByUser);
    if (userIdsWithCompletedTasks.length === 0) {
      console.log(completedTasksByUser);
    } else {
      console.log(completedTasksByUser);
    }
  }
});
