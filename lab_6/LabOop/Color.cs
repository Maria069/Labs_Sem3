namespace lab_6.LabOop {
    public class Color {
        private string color;
        public Color(string color = "") {
            this.color = color;
        }

        public string ColorName {
            get { return color; }
            set { color = value; }
        }
        public override string ToString() {
            return color;
        }
    }
}