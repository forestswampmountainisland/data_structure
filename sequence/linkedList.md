# 链表 (linkedList)

链表是一种非顺序的线性表，通过元素持有相邻元素的地址来联结到相邻元素。

关联前一个元素的指针叫头指针，关联后一个元素的指针叫尾指针。

![element](images/linked_list_element.png)

上图是链表元素的一种实现，data存储数据，next指向后一个元素

## 使用场景

常用于：

1. 存储一批元素且需要迭代访问的时候

比如说

一个进度条，有三个步骤，每个步骤是一个节点，整个是一个链表，前一个步骤结束才能进行后一个步骤。

相比于数组，链表无需事先申请存储空间或者resize。

## 常见实现

## 单链表

单链表有唯一的一个指针指向前一个元素或后一个元素，见[SingleLinkedList.py](../example/SingleLinkedList.py)

## 双链表

双链表有两个指针指向前一个元素和后一个元素

相比于单链表，双链表可以从后往前遍历还可以回溯以及逆序的遍历，但缺点是需要同时维护两个指针，见[DoubleLinkedList.py](../example/DoubleLinkedList.py)

## 循环链表

链表最后一个元素的尾指针指向第一个元素，这样可以一直迭代下去，见[CircularList.py](../example/CircularList.py)

## 操作

链表的空间复杂度是O(n)。

LinkedList实现见[这里](example/linkedList.py)

1. 初始化

```

list = LinkedList()

```

2. 添加

时间复杂度为O(n)

```

list.insert(data)

```

3. 删除

时间复杂度为O(n)

```

list.remove(i)

```

4. 更新


```

list.update(data, i)

```