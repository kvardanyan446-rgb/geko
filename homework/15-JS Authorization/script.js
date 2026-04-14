const users = [
  { username: "admin", password: "1234", isBlocked: false },
  { username: "john", password: "qwerty", isBlocked: true },
  { username: "anna", password: "pass", isBlocked: false }
];


function fuctional(input, username) {
  if (input === username) {
    return "Օգտատերը չի գտնվել";
  } else if (input === "e") {
    return "Սխալ գաղտնաբառ";
  } else if (input === "E") {
    return "Օգտատերը արգելափակված է";
  } else {
    return `Բարի գալուստ, ${username}`;
  }
}




