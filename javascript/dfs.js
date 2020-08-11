// Do not edit the class below except
// for the depthFirstSearch method.
// Feel free to add new properties
// and methods to the class.
class Node {
  constructor(name) {
    this.name = name;
    this.children = [];
  }

  addChild(name) {
    this.children.push(new Node(name));
    return this;
  }

  depthFirstSearch(array) {
    array.push(this.name);
    const nodeChildren = [];
    for (let i = this.children.length - 1; i >= 0; i--) {
      nodeChildren.push(this.children[i]);
    }
    console.log(nodeChildren);
    while (nodeChildren.length > 0) {
      const node = nodeChildren.pop();
      node.depthFirstSearch(array);
    }
    return array;
  }
}

// Do not edit the line below.
exports.Node = Node;
