import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import java.awt.GridLayout;
import java.awt.GridBagLayout;
import javax.swing.JLabel;
import java.awt.Font;
import javax.swing.JList;
import javax.swing.SwingConstants;
import javax.swing.JComboBox;
import javax.swing.JButton;
import javax.swing.ImageIcon;
import javax.swing.UIManager;
import javax.swing.DefaultComboBoxModel;
import javax.swing.JTextField;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class Prototipo extends JFrame {

	private JPanel contentPane;
	private JTextField textField;
	private JTextField textField_1;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Prototipo frame = new Prototipo();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public Prototipo() {
		setResizable(false);
		ImageIcon imgMap = new ImageIcon("./images/100%.jpg");
		ImageIcon imgMap75 = new ImageIcon("./images/50%.jpg");
		ImageIcon imgMapForward = new ImageIcon("./images/100%2.jpg");
		ImageIcon imgChart = new ImageIcon("images/pie chart.jpg");
		setTitle("CiberBulling Analysis");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 775, 595);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(new BorderLayout(0, 0));
		
		JPanel mapPanel = new JPanel();
		contentPane.add(mapPanel, BorderLayout.WEST);
		mapPanel.setLayout(new BorderLayout(0, 0));
		
		JPanel auxPan = new JPanel();
		mapPanel.add(auxPan, BorderLayout.SOUTH);
		auxPan.setLayout(new GridLayout(2, 2, 0, 0));
		
		JLabel lblNewLabel = new JLabel("Zoom");
		lblNewLabel.setForeground(UIManager.getColor("CheckBox.foreground"));
		lblNewLabel.setBackground(UIManager.getColor("CheckBox.highlight"));
		auxPan.add(lblNewLabel);
		lblNewLabel.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel.setFont(new Font("Tahoma", Font.PLAIN, 17));
		
		JComboBox cbtime = new JComboBox();
		cbtime.setFont(new Font("Tahoma", Font.PLAIN, 17));
		cbtime.setModel(new DefaultComboBoxModel(new String[] {"*Month"}));
		cbtime.setToolTipText("\r\n");
		auxPan.add(cbtime);
		JLabel label_1 = new JLabel("");
		JButton btnNewButton_1 = new JButton("Forward->");
		JButton btnNewButton = new JButton("<- Back");
		JComboBox cbZoom = new JComboBox();
		cbZoom.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				if((cbZoom.getSelectedItem() +"").equals("25%")) {
					btnNewButton.setEnabled(false);
					btnNewButton_1.setEnabled(true);
					label_1.setIcon(imgMap75);
				}
			}
		});
		cbZoom.setFont(new Font("Tahoma", Font.PLAIN, 18));
		cbZoom.setModel(new DefaultComboBoxModel(new String[] {"100%", "25%"}));
		auxPan.add(cbZoom);
		
		JPanel panelTime = new JPanel();
		auxPan.add(panelTime);
		panelTime.setLayout(new GridLayout(0, 2, 0, 0));

		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				btnNewButton.setEnabled(false);
				btnNewButton_1.setEnabled(true);
				label_1.setIcon(imgMap);
			}
		});
		btnNewButton.setEnabled(false);
		btnNewButton.setFont(new Font("Tahoma", Font.PLAIN, 15));
		
		panelTime.add(btnNewButton);
		
		
		btnNewButton_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				btnNewButton.setEnabled(true);
				btnNewButton_1.setEnabled(false);
				label_1.setIcon(imgMapForward);
				cbZoom.setSelectedIndex(0);
			}
		});
		btnNewButton_1.setFont(new Font("Tahoma", Font.PLAIN, 15));
		panelTime.add(btnNewButton_1);
		
		JLabel label = new JLabel("");
		mapPanel.add(label, BorderLayout.CENTER);
		
		JLabel label_3 = new JLabel("");
		mapPanel.add(label_3, BorderLayout.WEST);
		
		JPanel panel = new JPanel();
		mapPanel.add(panel, BorderLayout.CENTER);
		panel.setLayout(new GridLayout(0, 1, 0, 0));
		
		
		label_1.setBackground(UIManager.getColor("CheckBox.highlight"));
		panel.add(label_1);
		label_1.setIcon(imgMap);
		
		
		JPanel chartsPanel = new JPanel();
		contentPane.add(chartsPanel, BorderLayout.CENTER);
		chartsPanel.setLayout(new GridLayout(2, 1, 0, 0));
		
		JLabel label_2 = new JLabel("");
		label_2.setIcon(imgChart);
		chartsPanel.add(label_2);
		
		JPanel auxPan1 = new JPanel();
		chartsPanel.add(auxPan1);
		auxPan1.setLayout(new GridLayout(4, 0, 0, 0));
		
		JLabel lblNewLabel_1 = new JLabel("Variabilidad dinamica");
		lblNewLabel_1.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel_1.setFont(new Font("Tahoma", Font.PLAIN, 19));
		auxPan1.add(lblNewLabel_1);
		
		textField = new JTextField();
		textField.setHorizontalAlignment(SwingConstants.CENTER);
		textField.setFont(new Font("Tahoma", Font.PLAIN, 17));
		textField.setText("0.59");
		textField.setEditable(false);
		auxPan1.add(textField);
		textField.setColumns(10);
		
		JLabel lblNewLabel_2 = new JLabel("Puntaje de Ofensas");
		lblNewLabel_2.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel_2.setFont(new Font("Tahoma", Font.PLAIN, 19));
		auxPan1.add(lblNewLabel_2);
		
		textField_1 = new JTextField();
		textField_1.setHorizontalAlignment(SwingConstants.CENTER);
		textField_1.setFont(new Font("Tahoma", Font.PLAIN, 17));
		textField_1.setText("10%");
		textField_1.setEditable(false);
		auxPan1.add(textField_1);
		textField_1.setColumns(10);
	}

}
