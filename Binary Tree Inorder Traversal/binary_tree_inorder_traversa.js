var inorderTraversal = function(root) {
    if (!root) {
        return [];
    }

    const leftValues = inorderTraversal(root.left);

    const currentValue = [root.val];

    const rightValues = inorderTraversal(root.right);
    return [...leftValues, ...currentValue, ...rightValues];
};