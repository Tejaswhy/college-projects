import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.io.*;
import java.util.*;

public class MultiSubjectAttendance extends JFrame {
    private JTextField nameField;
    private JTable table;
    private DefaultTableModel model;
    private JComboBox<String> subjectBox;

    private static final String STUDENT_FILE = "students.txt";
    private static final String[] SUBJECTS = {
        "Probability Theory and Statistical Methods", "Object Oriented Programming", "Operating System", "Web Technology", 
        "Software Engineering", "Computer Networks", "Intenet of Things", "Life Skills for Engineers"
    };

    public MultiSubjectAttendance() {
        setTitle("Multi-Subject Attendance System");
        setSize(700, 500);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout());

        // 🔹 Top Panel (Subject selection and add student)
        JPanel topPanel = new JPanel(new FlowLayout());
        topPanel.add(new JLabel("Select Subject:"));
        subjectBox = new JComboBox<>(SUBJECTS);
        topPanel.add(subjectBox);

        topPanel.add(new JLabel("Student Name:"));
        nameField = new JTextField(12);
        topPanel.add(nameField);

        JButton addBtn = new JButton("Add Student");
        JButton presentBtn = new JButton("Mark Present");
        JButton absentBtn = new JButton("Mark Absent");
        JButton saveBtn = new JButton("Save Attendance");

        topPanel.add(addBtn);
        topPanel.add(presentBtn);
        topPanel.add(absentBtn);
        topPanel.add(saveBtn);

        add(topPanel, BorderLayout.NORTH);

        // 🔹 Table setup
        model = new DefaultTableModel(new String[]{"Name", "Attendance"}, 0);
        table = new JTable(model);
        add(new JScrollPane(table), BorderLayout.CENTER);

        // Load student list
        loadStudents();

        // 🔹 Select the first row automatically (if exists)
        if (model.getRowCount() > 0) {
            table.setRowSelectionInterval(0, 0);
        }

        // 🔹 Button Actions
        addBtn.addActionListener(e -> addStudent());
        presentBtn.addActionListener(e -> markAttendance("Present"));
        absentBtn.addActionListener(e -> markAttendance("Absent"));
        saveBtn.addActionListener(e -> saveAttendance());
    }

    private void addStudent() {
        String name = nameField.getText().trim();
        if (!name.isEmpty()) {
            model.addRow(new Object[]{name, "Not Marked"});
            saveStudentToFile(name);
            nameField.setText("");

            // Automatically select the newly added student
            int lastRow = model.getRowCount() - 1;
            table.setRowSelectionInterval(lastRow, lastRow);
        } else {
            JOptionPane.showMessageDialog(this, "Enter a student name!");
        }
    }

    private void markAttendance(String status) {
        int row = table.getSelectedRow();
        if (row != -1) {
            // Mark attendance for the selected student
            model.setValueAt(status, row, 1);

            // Automatically move to next row if available
            if (row + 1 < table.getRowCount()) {
                table.setRowSelectionInterval(row + 1, row + 1);
            } else {
                // If it's the last row, clear selection
                table.clearSelection();
                JOptionPane.showMessageDialog(this, "✅ All students marked!");
            }
        } else {
            JOptionPane.showMessageDialog(this, "Select a student first!");
        }
    }

    private void saveAttendance() {
        String subject = subjectBox.getSelectedItem().toString();
        String fileName = "attendance_" + subject + ".txt";

        try (FileWriter writer = new FileWriter(fileName)) {
            writer.write("Subject: " + subject + "\n");
            writer.write("=========================\n");
            for (int i = 0; i < model.getRowCount(); i++) {
                writer.write(model.getValueAt(i, 0) + " - " + model.getValueAt(i, 1) + "\n");
            }
            JOptionPane.showMessageDialog(this, "Attendance saved for " + subject + "!");
        } catch (IOException e) {
            JOptionPane.showMessageDialog(this, "Error saving attendance!");
        }
    }

    private void saveStudentToFile(String name) {
        try (FileWriter writer = new FileWriter(STUDENT_FILE, true)) {
            writer.write(name + "\n");
        } catch (IOException e) {
            JOptionPane.showMessageDialog(this, "Error saving student!");
        }
    }

    private void loadStudents() {
        File file = new File(STUDENT_FILE);
        if (file.exists()) {
            try (Scanner scanner = new Scanner(file)) {
                while (scanner.hasNextLine()) {
                    String name = scanner.nextLine().trim();
                    if (!name.isEmpty()) {
                        model.addRow(new Object[]{name, "Not Marked"});
                    }
                }
            } catch (FileNotFoundException e) {
                JOptionPane.showMessageDialog(this, "Error loading students!");
            }
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new MultiSubjectAttendance().setVisible(true));
    }
}
