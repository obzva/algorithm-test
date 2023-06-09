/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function (root) {
  function rec(node, leftLimit, rightLimit) {
    if (node === null) {
      return true;
    }
    if (leftLimit >= node.val || node.val >= rightLimit) {
      return false;
    }
    return (
      rec(node.left, leftLimit, node.val) &&
      rec(node.right, node.val, rightLimit)
    );
  }
  return rec(root, Number.MIN_SAFE_INTEGER, Number.MAX_SAFE_INTEGER);
};
