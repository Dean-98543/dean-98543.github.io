---
layout: markdown
---


# Git协同开发

Git是一个分布式版本控制系统，它能够帮助开发者管理代码的版本，并跟踪代码的修改历史。下面是一些使用github进行协同开发基本的一些使用命令：

1. 将项目仓库clone到本地：

   ```shell
   git clone [仓库URL]
   ```

   > 注：如若涉及到用户配置信息的问题，可参考网址[Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)使用个人访问令牌PAT进行认证

2. 创建一个新分支，并切换到该分支（建议分支命名规范：[姓名拼音缩写_当前任务描述]）：

   ```shell
   git checkout -b [新分支名]
   git add .
   ```

3. 进入项目目录，拉取远程主分支最新代码：

   ```shell
   git pull origin main
   ```

4. 开发功能（例如在tools目录下新建了func.py文件）

5. 将更改添加到缓存区：

   ```shell
   git add tools/func.py
   ```

6. 保存更改到本地git：

   ```shell
   git commit -m "Add func.py"
   ```

7. 拉取远程主分支，确保其最新：

   ```shell
   git pull origin main
   ```

8. 推送该新分支到远程：

   1. 或者将本地的某个分支的改动推送到远程的某一个分支：

9. 上一步成功后，会返回一个链接，访问该链接提交pull request

10. 填写request title 和 description，创建pull request

11. reviewer检查该request无误之后，将该request merge到main分支

12. 本地切换到主分支并查看当前分支：

13. 更新本地主分支

14. 删除本地刚才新建的分支：

15. 

16. # 1

17. ## 2

18. ### 3

19. #### 4

20. ##### 5

21. ###### 6

22. 7




$$
x = y^2
$$






