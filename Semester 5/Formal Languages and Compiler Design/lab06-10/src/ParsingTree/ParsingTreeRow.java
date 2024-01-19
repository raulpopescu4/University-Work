package ParsingTree;

public class ParsingTreeRow {

    private Integer index;
    private String info;
    private ParsingTreeRow parent;
    private ParsingTreeRow rightSibling;
    private ParsingTreeRow leftChild;
    private Integer level;

    public ParsingTreeRow(String info) {
        this.info = info;
    }

    public ParsingTreeRow(Integer index, String info, ParsingTreeRow parent, ParsingTreeRow rightSibling, ParsingTreeRow leftChild, Integer level) {
        this.index = index;
        this.info = info;
        this.parent = parent;
        this.rightSibling = rightSibling;
        this.leftChild = leftChild;
        this.level = level;
    }

    public Integer getIndex() {
        return index;
    }

    public void setIndex(Integer index) {
        this.index = index;
    }

    public String getInfo() {
        return info;
    }

    public void setInfo(String info) {
        this.info = info;
    }

    public ParsingTreeRow getParent() {
        return parent;
    }

    public void setParent(ParsingTreeRow parent) {
        this.parent = parent;
    }

    public ParsingTreeRow getRightSibling() {
        return rightSibling;
    }

    public void setRightSibling(ParsingTreeRow rightSibling) {
        this.rightSibling = rightSibling;
    }

    public ParsingTreeRow getLeftChild() {
        return leftChild;
    }

    public void setLeftChild(ParsingTreeRow leftChild) {
        this.leftChild = leftChild;
    }

    public Integer getLevel() {
        return level;
    }

    public void setLevel(Integer level) {
        this.level = level;
    }

    @Override
    public String toString() {
        return "ParsingTreeNode{" +
                "index=" + index +
                ", info='" + info + '\'' +
                ", leftChild=" + (leftChild != null ? leftChild.getIndex() : -1) +
                ", rightSibling=" + (rightSibling != null ? rightSibling.getIndex() : -1) +
                ", parent=" + (parent != null ? parent.getIndex() : -1) +
                ", level=" + level +
                '}';
    }
}
