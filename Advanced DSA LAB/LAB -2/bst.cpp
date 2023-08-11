#include<iostream>
#include<vector>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
    
};


TreeNode* insertNode(TreeNode* root, int value) {
    if (root == nullptr) {
        return new TreeNode(value);
    }

    if (value < root->val) {
        root->left = insertNode(root->left, value);
    } else if (value > root->val) {
        root->right = insertNode(root->right, value);
    }

    return root;
}


TreeNode* buildBST() {
    TreeNode* root = nullptr;
    int n;
    cout << "Enter the number of nodes: ";
    cin >> n;

    for (int i = 0; i < n; ++i) {
        int value;
        cout << "Enter the "<<i+1<<"th node value - ";
        cin >> value;
        root = insertNode(root, value);
    }

    return root;
}


vector<int> ans;




void inorder(TreeNode* node){
    if(node->left) inorder(node->left);
    ans.push_back(node->val);
    if(node->right) inorder(node->right);
}



int main(){
    TreeNode* node = buildBST();
    
    inorder(node);

    cout<<"The inorder traversal is : ";

    for(int i=0;i<ans.size();i++){
        cout<<ans[i]<<", ";
    }



    cout<<endl;
    return 0;
}